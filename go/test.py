import cv2
import numpy as np
from draw_go_table import drawboard  # นำเข้าฟังก์ชัน drawboard จากไฟล์ draw_go_table.py

def detect_and_update_board(board, transformed_region):
    gray_region = cv2.cvtColor(transformed_region, cv2.COLOR_BGR2GRAY)

    white_color = np.array([255, 255, 255])
    black_color = np.array([0, 0, 0])
    background_color = np.array([19, 104, 164])

    # สร้างภาพที่เน้นสีขาว (Go สีขาว) โดยหาสีที่ใกล้เคียง
    white_mask = cv2.inRange(transformed_region, white_color - 30, white_color + 30)

    # สร้างภาพที่เน้นสีดำ (Go สีดำ) โดยหาสีที่ใกล้เคียง
    black_mask = cv2.inRange(transformed_region, black_color - 30, black_color + 30)

    # สร้างภาพที่เน้นสีพื้นหลัง (ช่องว่าง) โดยหาสีที่ใกล้เคียง
    background_mask = cv2.inRange(transformed_region, background_color - 30, background_color + 30)

    # ทำการตรวจจับ Go สีขาว
    white_contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ทำการตรวจจับ Go สีดำ
    black_contours, _ = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ทำการตรวจจับช่องว่าง
    background_contours, _ = cv2.findContours(background_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ล้างบอร์ดเกม
    board.fill(0)

    # อัปเดตข้อมูลบอร์ด Go จาก Go สีขาว
    for contour in white_contours:
        if cv2.contourArea(contour) > 100:  # ตั้งค่าค่าที่เหมาะสมสำหรับขนาดของ Go
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                row = min(cY // (transformed_region.shape[0] // 9), 8)
                col = min(cX // (transformed_region.shape[1] // 9), 8)

                board[row, col] = 2  # 2 แทน Go สีขาว


    # อัปเดตข้อมูลบอร์ด Go จาก Go สีดำ
    for contour in black_contours:
        if cv2.contourArea(contour) > 100:  # ตั้งค่าค่าที่เหมาะสมสำหรับขนาดของ Go
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                row = min(cY // (transformed_region.shape[0] // 9), 8)
                col = min(cX // (transformed_region.shape[1] // 9), 8)

                board[row, col] = 1  # 1 แทน Go สีดำ

    # สร้างรูปภาพของบอร์ด Go ที่อัปเดตแล้ว
    updated_table = drawboard(board.T)
    return updated_table

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    T = None

    if not cap.isOpened():
        print('Error: Could not open the camera.')
        return -1

    board = np.zeros((9, 9), dtype=int)  # สร้างบอร์ดเริ่มต้น

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

            cv2.imshow(" Crop Table Go!", transformed_region)

            # Detect and update the board from the transformed_region
            updated_table = detect_and_update_board(board, transformed_region)

            # Show the updated table
            cv2.imshow(' Visual-Go table!', updated_table)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
