import cv2
import os
import time

# Open the webcam
cap = cv2.VideoCapture(1)  # 0 indicates the default camera (usually the built-in webcam)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a directory to save frames
output_folder = 'live_frames'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

frame_index = 0
capture_interval = 0.2  # Capture every 0.1 seconds (10 frames per second)
last_capture_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    current_time = time.time()
    if current_time - last_capture_time >= capture_interval:
        # Save the frame
        frame_filename = f"{output_folder}/frame_{frame_index:04d}.jpg"
        cv2.imwrite(frame_filename, frame)
        frame_index += 1

        last_capture_time = current_time

    # Display the frame
    cv2.imshow("Live Video", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
