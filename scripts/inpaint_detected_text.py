# Author: Felipe Parodi
# Date: 2023-05-19
# Project: MacFace
# Description: This script detects text in images and outputs the inpainted image.
# Usage: python inpaint_detected_text.py --input-dir /path/to/images

import os
import shutil
import cv2
import numpy as np
import argparse
from mmocr.apis import MMOCRInferencer

def main():
  # Argument parsing
  parser = argparse.ArgumentParser(description='Inference and inpaint images.')
  parser.add_argument('input_dir', type=str, help='Input directory with images')
  args = parser.parse_args()

  # Define input and output directories
  input_dir = args.input_dir
  text_detected_dir = os.path.join(input_dir, 'images_with_text')
  text_inpainted_dir = os.path.join(input_dir, 'images_with_text_inpainted')

  # Create output directories if they don't exist
  os.makedirs(text_detected_dir, exist_ok=True)
  os.makedirs(text_inpainted_dir, exist_ok=True)

  # Initialize the MMOCRInferencer
  infer = MMOCRInferencer(det='dbnetpp', rec='svtr-small')

  # Iterate over all images in the input directory
  for filename in os.listdir(input_dir):
      if filename.endswith(".jpg") or filename.endswith(".png"):
          img_path = os.path.join(input_dir, filename)

          # Perform text detection
          result = infer(img_path, return_vis=True)
          polygons = result['predictions'][0]['det_polygons']

          if polygons:  # If text is detected
              # Move image with detected text to text_detected_dir
              shutil.move(img_path, os.path.join(text_detected_dir, filename))

              # Load the image
              img = cv2.imread(img_path)
              img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

              # Create a mask for the detected text areas
              mask = np.zeros(img.shape[:2], dtype=np.uint8)
              for polygon in polygons:
                  polygon = np.array(polygon, np.int32).reshape((-1,1,2))
                  cv2.fillPoly(mask, [polygon], color=255)

              # Perform inpainting
              inpainted_img = cv2.inpaint(img, mask, 100, cv2.INPAINT_NS)

              # Save the inpainted image to the text_inpainted_dir
              inpainted_img_path = os.path.join(text_inpainted_dir, filename)
              cv2.imwrite(inpainted_img_path, cv2.cvtColor(inpainted_img, cv2.COLOR_RGB2BGR))
              
if __name__ == "__main__":
  main()
