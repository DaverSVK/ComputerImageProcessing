import math

import numpy as np
import cv2

def konvoLUCIA(image, kernel):
    kernel_height, kernel_width = kernel.shape

    out_height = (image.shape[0] - kernel_height)
    out_width = (image.shape[1] - kernel_width)

    im_split = cv2.split(image)
    output = np.empty((out_height, out_width), dtype=np.uint8)

    for y in range(0, out_height):
        for x in range(0, out_width):
            output[y, x] = np.sum(image[y:y+kernel_height, x:x+kernel_width]*kernel).astype("int")

    return output

maska = (1/159)*np.array([
    [2, 4, 5, 4, 2],
    [4, 9, 12, 9, 4],
    [5, 12, 15, 12, 5],
    [4, 9, 12, 9, 4],
    [2, 4, 5, 4, 2]
])
maska2 = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])
maska3 = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])

obrazek = cv2.imread("funny_japanese.png")

obrazekCV = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
obrazekMy = konvoLUCIA(obrazekCV, maska)
obrazekVert = konvoLUCIA(obrazekMy, maska3)
obrazekHoriz = konvoLUCIA(obrazekMy, maska2)
obrazekMy = obrazekVert

obrazekNOT = cv2.filter2D(src=obrazekCV, ddepth=-1, kernel=maska3)

cv2.imshow("obrazekMy", obrazekMy)
cv2.imshow("obrazekCV", obrazekNOT)
cv2.waitKey(0)

cv2.Canny()
