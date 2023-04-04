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

from mmpose.apis import (
    inference_top_down_pose_model,
    init_pose_model,
    process_mmdet_results,
    vis_pose_result,
)

start_time = time.time()


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--input-dir", type=str, help="path to images")
    parser.add_argument("--output-dir", type=str, help="path to the output directory")
    parser.add_argument("save_img_with_bbox", type=bool, help="save output with bbox")
    parser.add_argument("--device", default="cuda:0", type=str, help="device to use")
    args = parser.parse_args()

    out_dir = args.output_dir
    device = args.device
    img_dir = args.input_dir

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    os.makedirs(out_dir + "/viz", exist_ok=True)
    os.makedirs(out_dir + "/annotations", exist_ok=True)

    out_json_file = out_dir + "/annotations/instances_labels_f68.json"
    print(out_json_file)

    det_config = (
        "/mmdetection/fparodi/macface/results/ssd300-macface/ssd300_wider_face.py"
    )
    # det_checkpoint = "/mmpose/fparodi/macface/results/ssd300-macface/latest.pth"
    det_checkpoint = "/mmdetection/fparodi/macface/results/ssd300-total-ext/latest.pth"
    det_model = init_detector(det_config, det_checkpoint, device=device)

    pose_config = "/mmpose/configs/face/2d_kpt_sview_rgb_img/topdown_heatmap/ \
                    coco_wholebody_face/mobilenetv2_coco_wholebody_face_256x256.py"
    pose_checkpoint = "https://download.openmmlab.com/mmpose/face/mobilenetv2/ \
                      mobilenetv2_coco_wholebody_face_256x256-4a3f096e_20210909.pth"
    pose_model = init_pose_model(pose_config, pose_checkpoint, device=device)

    categories = [
        {
            "id": 1,
            "name": "face",
            "supercategory": "face",
            "keypoints": [  # 68 keypoints from coco-wholebody-face:
                "face-0",
                "face-1",
                "face-2",
                "face-3",
                "face-4",
                "face-5",
                "face-6",
                "face-7",
                "face-8",
                "face-9",
                "face-10",
                "face-11",
                "face-12",
                "face-13",
                "face-14",
                "face-15",
                "face-16",
                "face-17",
                "face-18",
                "face-19",
                "face-20",
                "face-21",
                "face-22",
                "face-23",
                "face-24",
                "face-25",
                "face-26",
                "face-27",
                "face-28",
                "face-29",
                "face-30",
                "face-31",
                "face-32",
                "face-33",
                "face-34",
                "face-35",
                "face-36",
                "face-37",
                "face-38",
                "face-39",
                "face-40",
                "face-41",
                "face-42",
                "face-43",
                "face-44",
                "face-45",
                "face-46",
                "face-47",
                "face-48",
                "face-49",
                "face-50",
                "face-51",
                "face-52",
                "face-53",
                "face-54",
                "face-55",
                "face-56",
                "face-57",
                "face-58",
                "face-59",
                "face-60",
                "face-61",
                "face-62",
                "face-63",
                "face-64",
                "face-65",
                "face-66",
                "face-67",
            ],
            "skeleton": [
                [0, 1],
                [1, 2],
                [2, 3],
                [3, 4],
                [4, 5],
                [5, 6],
                [6, 7],
                [7, 8],
                [8, 9],
                [9, 10],
                [10, 11],
                [11, 12],
                [12, 13],
                [13, 14],
                [14, 15],
                [15, 16],  # jawline
                [17, 18],
                [18, 19],
                [19, 20],
                [20, 21],  # left eyebrow
                [22, 23],
                [23, 24],
                [24, 25],
                [25, 26],  # right eyebrow
                [27, 28],
                [28, 29],
                [29, 30],  # nose bridge
                [31, 32],
                [32, 33],
                [33, 34],
                [34, 35],  # nose bottom
                [36, 37],
                [37, 38],
                [38, 39],
                [39, 40],
                [40, 41],
                [41, 36],  # left eye
                [42, 43],
                [43, 44],
                [44, 45],
                [45, 46],
                [46, 47],
                [47, 42],  # right eye
                [48, 49],
                [49, 50],
                [50, 51],
                [51, 52],
                [52, 53],
                [53, 54],
                [54, 55],
                [55, 56],
                [56, 57],
                [57, 58],
                [58, 59],
                [59, 48],  # outer lip
                [60, 61],
                [61, 62],
                [62, 63],
                [63, 64],
                [64, 65],
                [65, 66],
                [66, 67],
                [67, 60],  # inner lip
            ],
        }
    ]

    img_anno_dict = {
        "categories": categories,
        "images": [],
        "annotations": [],
    }

    bbox_thr = 0.9
    kpt_thr = 0.5

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

        detection_results = process_mmdet_results(detection_results, 1)

        pose_results, _ = inference_top_down_pose_model(
            pose_model,
            img,
            detection_results,
            bbox_thr=bbox_thr,
            format="xyxy",
            dataset="COCOWholeBodyFaceDataset",
        )
        annotations_added = False

        for indx, i in enumerate(pose_results):
            if pose_results[indx]["bbox"][4] <= bbox_thr:
                continue
            pose_results[indx]["keypoints"][
                pose_results[indx]["keypoints"][:, 2] < kpt_thr, :3
            ] = 0
            pose_results[indx]["keypoints"][
                pose_results[indx]["keypoints"][:, 2] >= kpt_thr, 2
            ] = 2

            bbox_top_left_x = int(pose_results[indx]["bbox"][0])
            bbox_top_left_y = int(pose_results[indx]["bbox"][1])
            bbox_width = int(
                pose_results[indx]["bbox"][2] - pose_results[indx]["bbox"][0]
            )
            bbox_height = int(
                pose_results[indx]["bbox"][3] - pose_results[indx]["bbox"][1]
            )
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
                "keypoints": [
                    int(i) for i in pose_results[indx]["keypoints"].reshape(-1).tolist()
                ],
                "num_keypoints": len(pose_results[indx]["keypoints"]),
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
            if args.save_img_with_bbox:
                kpts = vis_pose_result(
                    pose_model,
                    detection_frame,
                    pose_results,
                    kpt_score_thr=kpt_thr,
                    show=False,
                    radius=2,
                )
            else:
                kpts = vis_pose_result(
                    pose_model,
                    img,
                    pose_results,
                    kpt_score_thr=kpt_thr,
                    show=False,
                    radius=2,
                )
            vis_file_name = (
                out_dir + "/viz/" + frame_id + str(frame_id_uniq) + "_vis.jpg"
            )
            cv2.imwrite(vis_file_name, kpts)

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
