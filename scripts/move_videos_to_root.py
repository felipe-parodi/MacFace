import os
import sys
import shutil

def move_files_to_root(root_path):
    for folder, _, files in os.walk(root_path):
        # Skip the root directory
        if folder == root_path:
            continue

        for file in files:
            # Check if the file is a video
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm')):
                file_path = os.path.join(folder, file)
                target_path = os.path.join(root_path, file)

                # Move the video file to the root directory
                shutil.move(file_path, target_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python move_videos_to_root.py <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    move_files_to_root(root_directory)
