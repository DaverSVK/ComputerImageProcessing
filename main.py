import math

import numpy as np
import cv2



# Assuming check_extended_neighboring_pixels function is defined elsewhere in your code.


def konvoLUCIA(image, kernel):
    kernel_height, kernel_width = kernel.shape

    out_height = (image.shape[0] - kernel_height)
    out_width = (image.shape[1] - kernel_width)

    im_split = cv2.split(image)
    output = np.empty((out_height, out_width), dtype=np.uint8)

    for y in range(0, out_height):
        for x in range(0, out_width):
            sumis = np.sum(image[y:y+kernel_height, x:x+kernel_width]*kernel).astype("int")
            if sumis<0:
                sumis=0
            output[y, x] = sumis

    return output
def vyhodnocovanieHran(image, threshold,theta):

    output = np.zeros_like(image, dtype=np.uint8)

    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            #Matica 3x3 chyba smer gradientu
            if(theta[i,j]<112.5 and theta[i,j]>=67.5) or (theta[i,j]<22.5 or theta[i,j]>=337.5):
                if (image[i, j] >= image[i-1:i+2, j].max()):
                    output[i, j] = image[i, j]
            elif(theta[i,j]<337.5 and theta[i,j]>=292.5) or (theta[i,j]<157.5 and theta[i,j]>=112.5):
                if (image[i, j] >= image[i-1, j-1]) and (image[i, j] >=image[i+1, j+1]):
                    output[i, j] = image[i, j]
            elif(theta[i,j]<67.5 and theta[i,j]>=22.5) or (theta[i,j]<247.5 and theta[i,j]>=202.5):
                if (image[i, j] >= image[i-1, j+1]) and (image[i, j] >=image[i+1, j-1]):
                    output[i, j] = image[i, j]
            else:
                if (image[i, j] >= image[i, j-1:j+1].max()):
                    output[i, j] = image[i, j]

    return output

def hysMARTIN(image, upper, lower):
    output = np.zeros_like(image, dtype=np.uint8)
    max_row, max_col = image.shape

    # Mark the strong edges
    strong_i, strong_j = np.where(image > upper)
    output[strong_i, strong_j] = 255

    # Mark the weak edges
    weak_i, weak_j = np.where((image >= lower) & (image <= upper))

    for i, j in zip(strong_i, strong_j):
        for ii in range(max(0, i - 1), min(i + 2, max_row)):
            # Loop over the neighboring columns
            for jj in range(max(0, j - 1), min(j + 2, max_col)):
                # Skip the center pixel itself
                if (ii, jj) == (i, j):
                    continue
                if image[ii, jj] > lower:
                    output[ii, jj] = 255
                else:
                    output[ii, jj] = 0

    return output




def hysTEREZA(image, upper, lower):
    # output = np.zeros_like(image, dtype=np.uint8)
    #
    # for i in range(1, image.shape[0] - 1):
    #     for j in range(1, image.shape[1] - 1):
    #         if (image[i,j] < lower):
    #             output[i, j] = 0
    #         if (image[i,j] > upper):
    #             output[i, j] = 255
    #
    # for i in range(1, image.shape[0] - 1):
    #     for j in range(1, image.shape[1] - 1):
    #         if (image[i,j] >= lower)and(image[i,j] <= upper):
    #             candidate = False
    #             neighbours = check_neighboring_pixels(output, i, j)
    #             for each in neighbours:
    #                 if each == 255:
    #                     candidate = True
    #             if candidate:
    #                 output[i,j] = 255
    output = np.zeros_like(image, dtype=np.uint8)

    # Mark the strong edges
    strong_i, strong_j = np.where(image > upper)
    output[strong_i, strong_j] = 255

    # Mark the weak edges
    weak_i, weak_j = np.where((image >= lower) & (image <= upper))

    for i, j in zip(weak_i, weak_j):
        neighbours = check_neighboring_pixels(output, i, j)
        if 255 in neighbours:
            output[i, j] = 255
        else:
            output[i, j] = 0

    return output


def check_neighboring_pixels(image, row, col):
    # Get the dimensions of the image
    max_row, max_col = image.shape

    # List to hold the values of the neighboring pixels
    neighbors = []

    # Loop over the neighboring rows
    for i in range(max(0, row - 1), min(row + 2, max_row)):
        # Loop over the neighboring columns
        for j in range(max(0, col - 1), min(col + 2, max_col)):
            # Skip the center pixel itself
            if (i, j) == (row, col):
                continue
            # Add the neighbor pixel value to the list
            neighbors.append(image[i, j])

    return neighbors


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

#obrazek = cv2.imread("Recources/Tanjiro.png")
obrazek = cv2.imread("Recources/Lenna.png")
obrazekCV = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
# obrazekMyor = cv2.GaussianBlur(obrazekCV,[5,5])
obrazekMy = konvoLUCIA(obrazekCV, maska)
obrazekVert = konvoLUCIA(obrazekMy, maska3)
obrazekHoriz = konvoLUCIA(obrazekMy, maska2)
sobelx = cv2.Sobel(obrazekMy,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(obrazekMy,cv2.CV_64F,0,1,ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
# obrazekVert = cv2.filter2D(src=obrazekMy, ddepth=-1, kernel=maska3)
# obrazekHoriz = cv2.filter2D(src=obrazekMy, ddepth=-1, kernel=maska2)

# obrazekMyG = abs(obrazekVert+obrazekHoriz)
# obrazekMyG = abs(sobelx)+abs(sobely)
obrazekMyG = np.hypot(sobelx,sobely).astype(np.uint8)
# theta = np.degrees(np.arctan(np.divide(obrazekVert, obrazekHoriz)))
theta = np.degrees(np.arctan(np.divide(sobelx, sobely)))
obrazekMY = vyhodnocovanieHran(obrazekMyG,0.8,theta)

obrazekNOT = cv2.filter2D(src=obrazekMy, ddepth=-1, kernel=maska3)
obrazekNOTC = cv2.Canny(obrazekMy, threshold1=100, threshold2=150)

obrazekTEREZA = hysTEREZA(obrazekMY, 110, 70)
obrazekMARTIN = hysMARTIN(obrazekMY, 150, 50)
cv2.imshow("obrazekyMG", obrazekMyG)
cv2.imshow("obrazekyM", obrazekMy)
cv2.imshow("obrazekMy", obrazekMY)
cv2.imshow("obrazekCV", obrazekNOT)
cv2.imshow("obrazekCVC", obrazekNOTC)
cv2.imshow("obrazekTEREZA", obrazekTEREZA)
#cv2.imshow("obrazekMARTIN", obrazekMARTIN)
cv2.waitKey(0)
