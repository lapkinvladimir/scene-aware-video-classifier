import os
import cv2
from ultralytics import YOLO

model = YOLO('yolov8m.pt')


def annotate_frames(video_path, output_dir):
    video_path = os.path.abspath(video_path)
    print(f"Using video file: {video_path}")

    if not os.path.exists(video_path):
        print(f"File {video_path} does not exist")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory {output_dir}")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video file or can't read the frame")
            break
        print(f"Processing frame {frame_count}")

        results = model(frame)

        annotated_frame = results.render()[0]

        output_file = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(output_file, annotated_frame)
        print(f"Saved frame {frame_count} to {output_file}")

        frame_count += 1

    cap.release()
    print("Processing complete")


video_paths = ["data/videos/house_5.mov"]
output_dirs = ["data/frames/house_5"]

for video_path, output_dir in zip(video_paths, output_dirs):
    annotate_frames(video_path, output_dir)
