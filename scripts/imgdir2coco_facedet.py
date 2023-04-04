# Author: Felipe Parodi
# Date: 2023-04-04
# Project: MacFace
# Description: This script converts a directory of images to a COCO json file with detection labels.
# Usage: python imgdir2coco_facedet.py --input-dir /path/to/images --output-dir /path/to/output

import argparse
import glob
import json
import os
import time

import cv2
import mmcv
import numpy as np
from mmdet.apis import inference_detector, init_detector

start_time = time.time()


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--input-dir", type=str, help="path to images")
    parser.add_argument("--output-dir", type=str, help="path to the output directory")
    parser.add_argument("--device", default="cuda:0", type=str, help="device to use")
    args = parser.parse_args()

    out_dir = args.output_dir
    device = args.device
    img_dir = args.input_dir

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    os.makedirs(out_dir + "/viz", exist_ok=True)
    os.makedirs(out_dir + "/annotations", exist_ok=True)

    out_json_file = out_dir + "/annotations/instances_labels_det68.json"
    print(out_json_file)

    det_config = (
        "/mmdetection/fparodi/macface/results/ssd300-macface/ssd300_wider_face.py"
    )
    # det_checkpoint = "/mmpose/fparodi/macface/results/ssd300-macface/latest.pth"
    det_checkpoint = "/mmdetection/fparodi/macface/results/ssd300-total-ext/latest.pth"
    det_model = init_detector(det_config, det_checkpoint, device=device)

    categories = [{"id": 1, "name": "face", "supercategory": "face"}]

    img_anno_dict = {
        "categories": categories,
        "images": [],
        "annotations": [],
    }

    bbox_thr = 0.9

    print("Total number of images: ", len(os.listdir(img_dir)))

    ann_uniq_id = int(0)

    for img in sorted(glob.glob(os.path.join(img_dir, "*.jpg"))):
        frame_id = os.path.basename(img)[:-4]

        try:
            img = mmcv.imread(img)
            height, width = img.shape[0], img.shape[1]
        except Exception:
            print("Could not read image: ", img)
            os.remove(img)
            continue

        detection_results = inference_detector(det_model, img)

        if not detection_results[0]:
            continue

        annotations_added = False

        for indx, i in enumerate(detection_results[0]):
            if i[4] < bbox_thr:
                continue
            bbox_top_left_x = int(i[0])
            bbox_top_left_y = int(i[1])
            bbox_width = int(i[2] - i[0])
            bbox_height = int(i[3] - i[1])

            bbox = [bbox_top_left_x, bbox_top_left_y, bbox_width, bbox_height]
            area = round(bbox_width * bbox_height, 2)
            center = [
                bbox_top_left_x + bbox_width / 2,
                bbox_top_left_y + bbox_height / 2,
            ]
            scale = [bbox_width / 200, bbox_height / 200]

            frame_id_uniq = int(frame_id) + np.random.randint(0, 1000000)

            images = {
                "file_name": frame_id + ".jpg",
                "height": height,
                "width": width,
                "id": frame_id_uniq,
            }

            annotations = {
                "area": area,
                "iscrowd": 0,
                "image_id": frame_id_uniq,
                "bbox": bbox,
                "center": center,
                "scale": scale,
                "category_id": 1,
                "id": ann_uniq_id,
            }

            img_anno_dict["annotations"].append(annotations)
            ann_uniq_id += 1
            annotations_added = True
            detection_frame = det_model.show_result(
                img, detection_results, score_thr=bbox_thr, show=False
            )
            vis_file_name = (
                out_dir + "/viz/" + frame_id + str(frame_id_uniq) + "bbox_vis.jpg"
            )
            cv2.imwrite(vis_file_name, detection_frame)

        if annotations_added:
            img_anno_dict["images"].append(images)

    print("Number of images added to COCO json: ", len(img_anno_dict["images"]))
    print(
        "Percentage of images detected: ",
        (len(img_anno_dict["images"]) / len(os.listdir(img_dir)) * 100),
    )

    with open(out_json_file, "w") as outfile:
        json.dump(img_anno_dict, outfile, indent=2)

    print("Time elapsed: ", time.time() - start_time)


if __name__ == "__main__":
    main()
