import cv2
import numpy as np


def drawboard(board):
    border = 7 * 3  # mm
    line = 21 * 3  # mm
    size = (border * 2 + line * 8)  # mm
    template_size = (size, size, 3)
    out = np.full(template_size, [19, 104, 164], dtype=np.uint8)
    for i in range(border, size, line):
        cv2.line(out, (border, i), (size-border, i), (0, 0, 0), 1)
        cv2.line(out, (i, border), (i, size-border), (0, 0, 0), 1)
    w = np.where(board == 2)
    for w1, w2 in zip(w[0], w[1]):
        x = w1 * line + border
        y = w2 * line + border
        cv2.circle(out, (x, y), line//2, (255, 255, 255), -1)
    b = np.where(board == 1)
    for b1, b2 in zip(b[0], b[1]):
        x = b1 * line + border
        y = b2 * line + border
        cv2.circle(out, (x, y), line//2, (0, 0, 0), -1)
    return out


if __name__ == '__main__':
    board = np.zeros((9, 9), dtype=int)
    black = ((1, 1, 1), (1, 2, 3))
    white = ((2, 3), (6, 7))
    board[black] = 1
    board[white] = 2
    table = drawboard(board)
    cv2.imshow('table', table)
    cv2.waitKey(0)
