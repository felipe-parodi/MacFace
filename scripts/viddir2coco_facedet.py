# Author: Felipe Parodi
# Date: 2023-04-05
# Project: MacFace
# Description: This script converts a directory of videos to a COCO json file with detection labels.
# Usage: python viddir2coco_facedet.py --input-dir /path/to/images --output-dir /path/to/output

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

def delete_oldest_checkpoint(out_json_file, max_checkpoints=5):
    checkpoint_files = sorted(glob.glob(out_json_file.replace(".json", "_checkpoint_*.json")))
    if len(checkpoint_files) > max_checkpoints:
        os.remove(checkpoint_files[0])

def save_checkpoint(img_anno_dict, out_json_file, checkpoint_count):
    checkpoint_file = out_json_file.replace(".json", f"_checkpoint_{checkpoint_count}.json")
    with open(checkpoint_file, "w") as outfile:
        json.dump(img_anno_dict, outfile, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--input-dir", type=str, help="path to images")
    parser.add_argument("--output-dir", type=str, help="path to the output directory")
    parser.add_argument("--bbox-thr", default=0.2, type=float, help="bbox threshold")
    parser.add_argument("--checkpoint-interval", default=10, type=int, help="checkpoint interval")
    parser.add_argument("--device", default="cuda:2", type=str, help="device to use")
    args = parser.parse_args()

    vid_dir = args.input_dir
    out_dir = args.output_dir
    bbox_thr = args.bbox_thr
    checkpoint_interval = args.checkpoint_interval
    device = args.device

    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(out_dir + "/imgs", exist_ok=True)
    os.makedirs(out_dir + "/viz", exist_ok=True)
    os.makedirs(out_dir + "/annotations", exist_ok=True)

    out_json_file = out_dir + "/annotations/yt_labels_facedet.json"
    print(out_json_file)

    det_config = (
        "/mmpose/fparodi/macface/results/ssd300-macface/ssd300_wider_face.py"
    )
    det_checkpoint = "/mmpose/fparodi/macface/results/ssd300-macface/latest.pth"
    # det_checkpoint = "/mmpose/fparodi/macface/results/ssd300-total-ext/latest.pth"
    det_model = init_detector(det_config, det_checkpoint, device=device)

    categories = [{"id": 1, "name": "face", "supercategory": "face"}]

    img_anno_dict = {
        "categories": categories,
        "images": [],
        "annotations": [],
    }

    video_list = os.listdir(vid_dir)
    print("Total number of videos: ", len(video_list))
    uniq_id_list = []
    frame_id_uniq_counter = 0
    ann_uniq_id = int(0)
    checkpoint_count = int(0)
    for vid_idx, vid in enumerate(video_list):
        if not vid.endswith(".mp4"):
            continue
        video = mmcv.VideoReader(vid_dir + vid)
        print(vid)
        for frame_id, cur_frame in enumerate(mmcv.track_iter_progress(video)):
            detection_results = inference_detector(det_model, cur_frame)
            height, width, _ = cur_frame.shape
            # bboxes = process
            if len(detection_results[0]) == 0:
                continue

        # if len(detection_results[0]) == 0:
        #     continue
            for i in range(len(detection_results[0])):
                if detection_results[0][i][4] < bbox_thr:
                    detection_results[0][i] = [0, 0, 0, 0, 0]

            annotations_added = False

            for indx, i in enumerate(detection_results[0]):

                if detection_results[0][indx][4] < bbox_thr:
                    continue
        
                bbox_top_left_x = detection_results[0][indx][0]
                bbox_top_left_y = detection_results[0][indx][1]
                bbox_width = detection_results[0][indx][2] - detection_results[0][indx][0]
                bbox_height = detection_results[0][indx][3] - detection_results[0][indx][1]
                
                bbox = [bbox_top_left_x, bbox_top_left_y, bbox_width, bbox_height]

                if bbox_width == 0 or bbox_height == 0:
                    continue
                elif bbox_width < 0 or bbox_height < 0:
                    continue
                # else if the box is outside the image, skip it
                elif bbox_top_left_x < 0 or bbox_top_left_y < 0:
                    continue
                elif bbox_top_left_x + bbox_width > width or bbox_top_left_y + bbox_height > height:
                    continue
                
                area = round(bbox_width * bbox_height, 2)
                center = [
                    bbox_top_left_x + bbox_width / 2,
                    bbox_top_left_y + bbox_height / 2,
                ]
                scale = [bbox_width / 200, bbox_height / 200]

                frame_id_uniq = np.random.randint(0, 200000000)
                while frame_id_uniq in uniq_id_list:
                    frame_id_uniq = np.random.randint(0, 200000000)
                uniq_id_list.append(frame_id_uniq)
                # frame_id_uniq = frame_id_uniq_counter
                # frame_id_uniq_counter += 1

                file_name = "yt_" + str(frame_id_uniq) + ".jpg"

                images = {
                    # "file_name": os.path.basename(vid)[:-4]
                    # + "_"
                    # + str(frame_id_uniq)
                    # + ".jpg",
                    "file_name": file_name,
                    "height": height,
                    "width": width,
                    "id": frame_id_uniq,
                }

                annotations = {
                    # convert everything to float
                    "area": float(area),
                    "iscrowd": 0,
                    "image_id": int(frame_id_uniq),
                    "bbox": [float(i) for i in bbox],
                    "center": [float(i) for i in center],
                    "scale": [float(i) for i in scale],
                    "category_id": 1,
                    "id": int(ann_uniq_id),
                }

                img_anno_dict["annotations"].append(annotations)
                ann_uniq_id += 1
                annotations_added = True

                raw_frame = (
                    out_dir
                    + "/imgs/"
                    + file_name
                )
                cv2.imwrite(raw_frame, cur_frame)
                detection_frame = det_model.show_result(
                    cur_frame, 
                    detection_results, score_thr=bbox_thr, show=False
                )
                viz_frame = (
                    out_dir
                    + "/viz/"
                    + file_name[:-4]
                    + "_bbox_vis.jpg"
                )
                cv2.imwrite(viz_frame, detection_frame)

            if annotations_added:
                img_anno_dict["images"].append(images)
                
        os.remove(os.path.join(vid_dir, vid))

        if (vid_idx + 1) % checkpoint_interval == 0:
            checkpoint_count += 1
            save_checkpoint(img_anno_dict, out_json_file, checkpoint_count)
            delete_oldest_checkpoint(out_json_file)

    print("Number of images added to COCO json: ", len(img_anno_dict["images"]))

    with open(out_json_file, "w") as outfile:
        json.dump(img_anno_dict, outfile, indent=2)

    print("Time elapsed: ", time.time() - start_time)


if __name__ == "__main__":
    main()
