import cv2
import os

def process_video(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        # Read frame by frame
        ret, frame = cap.read()

        # Break the loop if there are no more frames
        if not ret:
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Save the frame as an image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, gray_frame)

        frame_count += 1

    # Release the video capture object
    cap.release()
video_path = 'https://media.talkbank.org/fluency/Voices-AWS/reading/24fa.mp4'
output_folder = 'D:/Voices-AWS/reading/24fa'
process_video(video_path, output_folder)
