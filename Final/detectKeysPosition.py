import cv2
import numpy as np

# Global variables
mouse_position = (0, 0)

# Function to update mouse position
def update_mouse_position(event, x, y, flags, param):
    global mouse_position
    mouse_position = (x, y)

# Function to display keyboard layout and mouse position
def display_keyboard_layout():
    global mouse_position

    # Read the keyboard layout image
    keyboard_img = cv2.imread('keyboard_layout.jpg')

    # Get the image dimensions
    img_height, img_width = keyboard_img.shape[:2]

    # Calculate the window size to fit the image
    window_size = (img_width, img_height)

    # Create a window for the virtual keyboard
    cv2.namedWindow('Virtual Keyboard', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Virtual Keyboard', *window_size)
    cv2.imshow('Virtual Keyboard', keyboard_img)
    cv2.setMouseCallback('Virtual Keyboard', update_mouse_position)

    while True:
        # Display mouse position
        img_with_mouse_position = keyboard_img.copy()
        cv2.putText(img_with_mouse_position, f"Mouse Position: {mouse_position}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display the virtual keyboard with mouse position
        cv2.imshow('Virtual Keyboard', img_with_mouse_position)

        # Check if the windows should be closed
        key = cv2.waitKey(1)
        if key == 27:  # Esc key
            break

    # Release the virtual keyboard window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_keyboard_layout()
