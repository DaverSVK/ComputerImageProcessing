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
            # if(theta[i,j]<112.5 and theta[i,j]>=67.5)
            #     if (image[i, j] >= image[i-1:i+2, j].max()):
            #         output[i, j] = image[i, j]
            #         print(theta[i,j])
            # elif(theta[i,j]<67.5 and theta[i,j]>=22.5):
            if (image[i, j] >= image[i-1:i+2, j].max())or(image[i, j] >= image[i-1:i+2, j].max()):
                    output[i, j] = image[i, j]



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

obrazek = cv2.imread("Recources/nezuko.jpg")
obrazekCV = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
# obrazekMyor = cv2.GaussianBlur(obrazekCV,[5,5])
obrazekMy = konvoLUCIA(obrazekCV, maska)
obrazekVert = konvoLUCIA(obrazekMy, maska3)
obrazekHoriz = konvoLUCIA(obrazekMy, maska2)
# sobelx = cv2.Sobel(obrazekMy,cv2.CV_64F,1,0,ksize=3)
# # sobely = cv2.Sobel(obrazekMy,cv2.CV_64F,0,1,ksize=3)
# sobelx = np.uint8(np.absolute(sobelx))
# sobely = np.uint8(np.absolute(sobely))
# # obrazekMy = obrazekVert+obrazekHoriz
obrazekMyG = abs(obrazekVert+obrazekHoriz)
theta = np.degrees(np.arctan(np.divide(obrazekVert, obrazekHoriz)))
obrazekMY = vyhodnocovanieHran(obrazekMyG,0.8,theta)

obrazekNOT = cv2.filter2D(src=obrazekMy, ddepth=-1, kernel=maska3)
obrazekNOTC = cv2.Canny(obrazekMy, threshold1=100, threshold2=200)
cv2.imshow("obrazekyMG", obrazekMyG)
cv2.imshow("obrazekyM", obrazekMy)
cv2.imshow("obrazekMy", obrazekMY)
cv2.imshow("obrazekCV", obrazekNOT)
cv2.imshow("obrazekCVC", obrazekNOTC)
cv2.waitKey(0)
