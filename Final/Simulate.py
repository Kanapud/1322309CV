import cv2

# Function to draw a red square on the image
def draw_red_square(img, top_left, size):
    img_with_square = img.copy()
    bottom_right = (top_left[0] + size, top_left[1] + size)
    cv2.rectangle(img_with_square, top_left, bottom_right, (0, 0, 255), -1)
    return img_with_square

# Function to detect mouse clicks on the virtual keyboard
def detect_mouse_click(event, x, y, flags, param):
    global typed_text, keyboard_layout

    if event == cv2.EVENT_LBUTTONDOWN:
        for key, (key_x, key_y, key_w, key_h) in keyboard_layout.items():
            if key_x < x < key_x + key_w and key_y < y < key_y + key_h:
                typed_text += key
                print(f"Typed: {typed_text}")
                break

# Main function
def main():
    global typed_text, keyboard_layout, keyboard_img

    # Read the simulated keyboard image
    keyboard_img = cv2.imread('keyboard_layout.jpg')

    # Define the virtual keyboard layout
    keyboard_layout = {
        'Q': (111, 76, 50, 50),
        'W': (179, 76, 50, 50),
        'E': (246, 76, 50, 50),
        'R': (314, 76, 50, 50),
        'T': (382, 76, 50, 50),
        'Y': (449, 76, 50, 50),
        'U': (517, 76, 50, 50),
        'I': (585, 76, 50, 50),
        'O': (652, 76, 50, 50),
        'P': (720, 76, 50, 50),
        '[': (787, 76, 50, 50),
        ']': (855, 76, 50, 50),

        'A': (128, 143, 50, 50),
        'S': (196, 143, 50, 50),
        'D': (264, 143, 50, 50),
        'F': (331, 143, 50, 50),
        'G': (399, 143, 50, 50),
        'H': (466, 143, 50, 50),
        'J': (534, 143, 50, 50),
        'K': (602, 143, 50, 50),
        'L': (669, 143, 50, 50),

        'Z': (0, 0, 50, 50),
        'X': (0, 0, 50, 50),
        'C': (0, 0, 50, 50),
        'V': (0, 0, 50, 50),
        'B': (0, 0, 50, 50),
        'N': (0, 0, 50, 50),
        'M': (0, 0, 50, 50),
        # Add more keys as needed
    }

    # Initialize an empty string to store typed characters
    typed_text = ""

    # Draw the initial red square and display the typed text
    keyborder = draw_red_square(keyboard_img, (keyboard_layout['F'][0], keyboard_layout['F'][1]), size=50)

    # Create a window for the virtual keyboard
    cv2.namedWindow('Virtual Keyboard')
    cv2.imshow('Virtual Keyboard', keyborder)
    cv2.setMouseCallback('Virtual Keyboard', detect_mouse_click)

    while True:
        # Check if the windows should be closed
        key = cv2.waitKey(1)
        if key == 27:  # Esc key
            break

    # Release the virtual keyboard window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
