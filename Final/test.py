import cv2
import numpy as np

# Function to draw rectangles for each key on the virtual keyboard
def draw_keyboard(image, keyboard_layout):
    img_with_rectangles = image.copy()
    for key, (x, y, width, height) in keyboard_layout.items():
        cv2.rectangle(img_with_rectangles, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv2.putText(img_with_rectangles, key, (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    return img_with_rectangles

# Create a blank image as the virtual keyboard
virtual_keyboard = np.zeros((300, 800, 3), dtype=np.uint8)

# Define the virtual keyboard layout for a QWERTY keyboard with space bar and backspace
keyboard_layout = {
    'Q': (20, 20, 30, 30),
    'W': (70, 20, 30, 30),
    'E': (120, 20, 30, 30),
    'R': (170, 20, 30, 30),
    'T': (220, 20, 30, 30),
    'Y': (270, 20, 30, 30),
    'U': (320, 20, 30, 30),
    'I': (370, 20, 30, 30),
    'O': (420, 20, 30, 30),
    'P': (470, 20, 30, 30),

    'A': (45, 70, 30, 30),
    'S': (95, 70, 30, 30),
    'D': (145, 70, 30, 30),
    'F': (195, 70, 30, 30),
    'G': (245, 70, 30, 30),
    'H': (295, 70, 30, 30),
    'J': (345, 70, 30, 30),
    'K': (395, 70, 30, 30),
    'L': (445, 70, 30, 30),

    'Z': (70, 120, 30, 30),
    'X': (120, 120, 30, 30),
    'C': (170, 120, 30, 30),
    'V': (220, 120, 30, 30),
    'B': (270, 120, 30, 30),
    'N': (320, 120, 30, 30),
    'M': (370, 120, 30, 30),

    'SPACE': (120, 170, 230, 30),  # Space bar
    'BACKSPACE': (470, 170, 50, 30),  # Backspace
}

# Draw rectangles for each key on the virtual keyboard
image_with_rectangles = draw_keyboard(virtual_keyboard, keyboard_layout)

# Display the image with rectangles
cv2.imshow('Virtual Keyboard', image_with_rectangles)
cv2.waitKey(0)
cv2.destroyAllWindows()
