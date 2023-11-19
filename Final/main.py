import cv2
import numpy as np

# Function to detect changes in the keyboard region
def detect_typing(frame, prev_frame, keyboard_region):
    # Convert frames to grayscale for difference calculation
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prev_gray_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference between frames
    diff = cv2.absdiff(gray_frame, prev_gray_frame)

    # Apply threshold to focus on significant changes
    _, threshold_diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Use the keyboard region to identify typing
    typing_roi = threshold_diff[keyboard_region[1]:keyboard_region[3], keyboard_region[0]:keyboard_region[2]]

    # Count non-zero pixels (changed pixels) in the region
    change_count = cv2.countNonZero(typing_roi)

    return change_count > 100  # Adjust this threshold based on your setup

# Main function
def main():
    # Set up video capture
    cap = cv2.VideoCapture(0)

    # Define the keyboard region (adjust these values based on your setup)
    keyboard_region = (100, 200, 900, 500)

    # Create a window for real-time camera feed
    cv2.namedWindow('Real-time Camera Feed', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Real-time Camera Feed', 800, 600)

    # Create a window for displaying typed characters
    cv2.namedWindow('Typed Characters', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Typed Characters', 400, 200)

    # Read the first frame
    ret, prev_frame = cap.read()

    # Initialize an empty string to store typed characters
    typed_text = ""

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Detect typing on the simulated keyboard
        typing_detected = detect_typing(frame, prev_frame, keyboard_region)

        # Display the real-time camera feed
        cv2.imshow('Real-time Camera Feed', frame)

        # Display typed characters
        if typing_detected:
            typed_text += "A"  # Replace this with the actual character detected
            cv2.putText(frame, typed_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Typed Characters', frame)

        # Update the previous frame
        prev_frame = frame.copy()

        # Check if the windows should be closed
        key = cv2.waitKey(1)
        if key == 27:  # Esc key
            break

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    main()
