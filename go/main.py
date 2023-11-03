# import sys
# import math
# import cv2 as cv
# import numpy as np
#
# def main():
#     # Initialize the webcam
#     cap = cv.VideoCapture(0)  # 0 corresponds to the default camera
#
#     if not cap.isOpened():
#         print("Error opening webcam!")
#         return -1
#
#     while True:
#         # Capture a frame from the webcam
#         ret, frame = cap.read()
#
#         if not ret:
#             print("Error reading frame!")
#             break
#
#         # Convert the frame to grayscale
#         src = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#
#         # Apply Canny edge detection
#         dst = cv.Canny(src, 50, 200, None, 3)
#
#         # Copy edges to the images that will display the results in BGR
#         cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
#         cdstP = np.copy(cdst)
#
#         # Detect lines using Hough Line Transform
#         lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
#
#         if lines is not None:
#             for i in range(0, len(lines)):
#                 rho = lines[i][0][0]
#                 theta = lines[i][0][1]
#                 a = math.cos(theta)
#                 b = math.sin(theta)
#                 x0 = a * rho
#                 y0 = b * rho
#                 pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
#                 pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
#                 cv.line(cdst, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)
#
#         # Detect lines using Probabilistic Line Transform
#         linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
#
#         if linesP is not None:
#             for i in range(0, len(linesP)):
#                 l = linesP[i][0]
#                 cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)
#
#         # Display the results
#         cv.imshow("Webcam Feed", frame)
#         cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
#         cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
#
#         if cv.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Release the webcam and close OpenCV windows
#     cap.release()
#     cv.destroyAllWindows()
#
# if __name__ == "__main__":
#     main()

# import cv2
# import numpy as np
#
# def main():
#     # Open the default camera (camera index 0)
#     cap = cv2.VideoCapture(0)
#
#     if not cap.isOpened():
#         print('Error: Could not open the camera.')
#         return -1
#
#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()
#
#         if not ret:
#             print('Error: Could not read a frame.')
#             break
#
#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         # Apply Gaussian blur to reduce noise
#         blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
#         # Apply Canny edge detection
#         edges = cv2.Canny(blurred, 50, 150)
#
#         # Find contours in the edges
#         contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#         yellow_board = None
#
#         for contour in contours:
#             # Approximate the contour with a polygon
#             epsilon = 0.04 * cv2.arcLength(contour, True)
#             approx = cv2.approxPolyDP(contour, epsilon, True)
#
#             # If the contour has 4 vertices, it's likely a rectangle (board)
#             if len(approx) == 4:
#                 yellow_board = approx
#                 cv2.drawContours(frame, [yellow_board], 0, (0, 255, 0), 2)
#
#         if yellow_board is not None:
#             # Extract the region of interest (yellow board)
#             x, y, w, h = cv2.boundingRect(yellow_board)
#             roi = frame[y:y + h, x:x + w]
#
#             # Convert the ROI to grayscale
#             roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#
#             # Apply Canny edge detection on the yellow board
#             edges_board = cv2.Canny(roi_gray, 50, 150)
#
#             # Apply Hough Line Transform on the yellow board
#             lines = cv2.HoughLines(edges_board, 1, np.pi / 180, 150)
#
#             if lines is not None:
#                 for line in lines:
#                     rho, theta = line[0]
#                     a = np.cos(theta)
#                     b = np.sin(theta)
#                     x0 = a * rho
#                     y0 = b * rho
#                     x1 = int(x0 + 1000 * (-b))
#                     y1 = int(y0 + 1000 * (a))
#                     x2 = int(x0 - 1000 * (-b))
#                     y2 = int(y0 - 1000 * (a))
#                     cv2.line(roi, (x1, y1), (x2, y2), (0, 0, 255), 2)
#
#         # Show the frame with detected rectangles and lines
#         cv2.imshow("Camera Feed with Rectangles and Lines", frame)
#
#         # Exit the loop if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Release the camera and close all OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     main()

# import cv2
# import numpy as np
#
# def main():
#     # Open the default camera (camera index 0)
#     cap = cv2.VideoCapture(0)
#
#     if not cap.isOpened():
#         print('Error: Could not open the camera.')
#         return -1
#
#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()
#
#         if not ret:
#             print('Error: Could not read a frame.')
#             break
#
#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         # Apply Gaussian blur to reduce noise
#         blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
#         # Apply Canny edge detection
#         edges = cv2.Canny(blurred, 50, 150)
#
#         # Find contours in the edges
#         contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#         yellow_board = None
#
#         for contour in contours:
#             # Approximate the contour with a polygon
#             epsilon = 0.04 * cv2.arcLength(contour, True)
#             approx = cv2.approxPolyDP(contour, epsilon, True)
#
#             # If the contour has 4 vertices, it's likely a rectangle
#             if len(approx) == 4:
#                 cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
#
#                 # Check if the rectangle is yellow
#                 x, y, w, h = cv2.boundingRect(contour)
#                 roi = frame[y:y + h, x:x + w]
#
#                 hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#                 lower_yellow = np.array([20, 100, 100])
#                 upper_yellow = np.array([30, 255, 255])
#                 mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
#
#                 if cv2.countNonZero(mask) > 0:
#                     yellow_board = roi
#
#         if yellow_board is not None:
#             # Convert the yellow board to grayscale
#             yellow_gray = cv2.cvtColor(yellow_board, cv2.COLOR_BGR2GRAY)
#
#             # Apply Hough Line Transform on the yellow board
#             yellow_edges = cv2.Canny(yellow_gray, 50, 150)
#             yellow_lines = cv2.HoughLines(yellow_edges, 1, np.pi / 180, 150)
#
#             if yellow_lines is not None:
#                 for line in yellow_lines:
#                     rho, theta = line[0]
#                     a = np.cos(theta)
#                     b = np.sin(theta)
#                     x0 = a * rho
#                     y0 = b * rho
#                     pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
#                     pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
#                     cv2.line(yellow_board, pt1, pt2, (0, 0, 255), 3)
#
#         # Show the frame with detected rectangles and lines
#         cv2.imshow("Camera Feed with Rectangles and Lines", frame)
#
#         # Exit the loop if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Release the camera and close all OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     main()



# import cv2
# import numpy as np
#
# def main():
#     # Open the default camera (camera index 0)
#     cap = cv2.VideoCapture(0)
#
#     if not cap.isOpened():
#         print('Error: Could not open the camera.')
#         return -1
#
#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()
#
#         if not ret:
#             print('Error: Could not read a frame.')
#             break
#
#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         # Apply Gaussian blur to reduce noise
#         blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
#         # Apply Canny edge detection
#         edges = cv2.Canny(blurred, 50, 150)
#
#         # Find contours in the edges
#         contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#         yellow_board = None
#
#         for contour in contours:
#             # Approximate the contour with a polygon
#             epsilon = 0.04 * cv2.arcLength(contour, True)
#             approx = cv2.approxPolyDP(contour, epsilon, True)
#
#             # If the contour has 4 vertices, it's likely a rectangle
#             if len(approx) == 4:
#                 # Check if the rectangle is yellow
#                 x, y, w, h = cv2.boundingRect(contour)
#                 roi = frame[y:y + h, x:x + w]
#
#                 hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#                 lower_yellow = np.array([20, 100, 100])
#                 upper_yellow = np.array([30, 255, 255])
#                 mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
#
#                 if cv2.countNonZero(mask) > 0:
#                     cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
#                     yellow_board = roi
#
#         if yellow_board is not None:
#             # Convert the yellow board to grayscale
#             yellow_gray = cv2.cvtColor(yellow_board, cv2.COLOR_BGR2GRAY)
#
#             # Apply Hough Line Transform on the yellow board
#             yellow_edges = cv2.Canny(yellow_gray, 50, 150)
#             yellow_lines = cv2.HoughLines(yellow_edges, 1, np.pi / 180, 150)
#
#             if yellow_lines is not None:
#                 for line in yellow_lines:
#                     rho, theta = line[0]
#                     a = np.cos(theta)
#                     b = np.sin(theta)
#                     x0 = a * rho
#                     y0 = b * rho
#                     pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
#                     pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
#                     cv2.line(yellow_board, pt1, pt2, (0, 0, 255), 3)
#
#         # Show the frame with detected rectangles and lines
#         cv2.imshow("Camera Feed with Rectangles and Lines", frame)
#
#         # Exit the loop if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Release the camera and close all OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     main()

# # ของอาจารย์ต้น
# import cv2
# import numpy as np
#
#
# def drawboard(board):
#     border = 7 * 5  # mm
#     line = 21 * 5  # mm
#     size = (border * 2 + line * 8)  # mm
#     template_size = (size, size, 3)
#     out = np.full(template_size, [19, 104, 164], dtype=np.uint8)
#     for i in range(border, size, line):
#         cv2.line(out, (border, i), (size-border, i), (0, 0, 0), 1)
#         cv2.line(out, (i, border), (i, size-border), (0, 0, 0), 1)
#     w = np.where(board == 2)
#     for w1, w2 in zip(w[0], w[1]):
#         x = w1 * line + border
#         y = w2 * line + border
#         cv2.circle(out, (x, y), line//2, (255, 255, 255), -1)
#     b = np.where(board == 1)
#     for b1, b2 in zip(b[0], b[1]):
#         x = b1 * line + border
#         y = b2 * line + border
#         cv2.circle(out, (x, y), line//2, (0, 0, 0), -1)
#     return out
#
#
# if __name__ == '__main__':
#     board = np.zeros((9, 9), dtype=int)
#     black = ((1, 1, 1), (1, 2, 3))
#     white = ((2, 3), (6, 7))
#     board[black] = 1
#     board[white] = 2
#     table = drawboard(board)
#     cv2.imshow('table', table)
#     cv2.waitKey(0)

# Final
# import cv2
# import numpy as np
#
# def main():
#     # Open the default camera (camera index 0)
#     cap = cv2.VideoCapture(0)
#
#     if not cap.isOpened():
#         print('Error: Could not open the camera.')
#         return -1
#
#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()
#
#         if not ret:
#             print('Error: Could not read a frame.')
#             break
#
#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         # Apply Gaussian blur to reduce noise
#         blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
#         # Apply Canny edge detection
#         edges = cv2.Canny(blurred, 50, 150)
#
#         # Find contours in the edges
#         contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#         yellow_board = None
#
#         for contour in contours:
#             # Approximate the contour with a polygon
#             epsilon = 0.04 * cv2.arcLength(contour, True)
#             approx = cv2.approxPolyDP(contour, epsilon, True)
#
#             # If the contour has 4 vertices, it's likely a rectangle
#             if len(approx) == 4:
#                 # Check if the rectangle is yellow
#                 x, y, w, h = cv2.boundingRect(contour)
#                 roi = frame[y:y + h, x:x + w]
#
#                 hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#                 lower_yellow = np.array([20, 100, 100])
#                 upper_yellow = np.array([30, 255, 255])
#                 mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
#
#                 if cv2.countNonZero(mask) > 0:
#                     yellow_board = roi
#
#         if yellow_board is not None:
#             # Convert the yellow board to grayscale
#             yellow_gray = cv2.cvtColor(yellow_board, cv2.COLOR_BGR2GRAY)
#
#             # Apply Hough Line Transform on the yellow board
#             yellow_edges = cv2.Canny(yellow_gray, 50, 150)
#             yellow_lines = cv2.HoughLines(yellow_edges, 1, np.pi / 180, 150)
#
#             if yellow_lines is not None:
#                 for line in yellow_lines:
#                     rho, theta = line[0]
#                     a = np.cos(theta)
#                     b = np.sin(theta)
#                     x0 = a * rho
#                     y0 = b * rho
#                     pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
#                     pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
#                     cv2.line(yellow_board, pt1, pt2, (0, 0, 255), 3)
#
#         # Show the frame with detected rectangles and lines
#         if yellow_board is not None:
#             cv2.imshow("Yellow Board with Lines", yellow_board)
#
#         # Exit the loop if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Release the camera and close all OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     main()


import cv2
import numpy as np

def main():
    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    T = None

    if not cap.isOpened():
        print('Error: Could not open the camera.')
        return -1

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print('Error: Could not read a frame.')
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Canny edge detection
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if T is None:
            largest_area = 0
            largest_contour = None

            for contour in contours:
                # Calculate the area of the contour
                area = cv2.contourArea(contour)

                if area > largest_area:
                    largest_area = area
                    largest_contour = contour

            if largest_contour is not None:
                # Approximate the largest contour with a polygon
                epsilon = 0.04 * cv2.arcLength(largest_contour, True)
                approx = cv2.approxPolyDP(largest_contour, epsilon, True)

                # If the largest contour has 4 vertices, it's likely a rectangle
                if len(approx) == 4:
                    # Get the perspective transform
                    pts1 = np.float32(approx)
                    pts2 = np.float32([[0, 0], [500, 0], [500, 500], [0, 500]])  # Define the target rectangle
                    T = cv2.getPerspectiveTransform(pts1, pts2)

        if T is not None:
            transformed_region = cv2.warpPerspective(frame, T, (500, 500))

            cv2.imshow("transformed_region", transformed_region)


        # Show the frame with the largest rectangular contour
        cv2.imshow("Camera Feed with Largest Rectangle", frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()