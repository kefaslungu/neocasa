import cv2
import os

def snap_picture(save_path="captured_image.jpg"):
    cap = cv2.VideoCapture(0)  # Open the default camera

    if not cap.isOpened():
        return None, "Failed to access the camera."

    ret, frame = cap.read()
    cap.release()  # Release the camera

    if not ret:
        return None, "Failed to capture image."

    cv2.imwrite(save_path, frame)  # Save the image
    return save_path, None  # Return image path and no error
