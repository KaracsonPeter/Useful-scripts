import cv2
import os


def extract_frames(mp4_path, output_dir, every_nth_frame):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(mp4_path)
    if not cap.isOpened():
        print("Error: Unable to open video file")
        return

    frame_count = 0
    while True:
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break

        # Save every nth frame as an image file
        if frame_count % every_nth_frame == 0:
            frame_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            print(f"Saved frame {frame_count} as {frame_path}")

        frame_count += 1

    # Release the video capture object
    cap.release()


# Example usage
mp4_file_name = 'dogs_are_barking.mp4'
mp4_path = f"C:/path/to/your/mp4/file/{mp4_file_name}"
output_dir = "../output"
every_nth_frame = 1  # Create image from every nth frame of the video

extract_frames(mp4_path, output_dir, every_nth_frame)
