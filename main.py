from ximea import xiapi
import cv2
import numpy as np
### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###

#create instance for first connected camera
cam = xiapi.Camera()


#start communication
#to open specific device, use:
#cam.open_device_by_SN('41305651')
#(open by serial number)
print('Opening first camera...')
cam.open_device()

#settings
cam.set_exposure(10000)
cam.set_param('imgdataformat','XI_RGB32')
cam.set_param('auto_wb', 1)
print('Exposure was set to %i us' %cam.get_exposure())

#create instance of Image to store image data and metadata
img = xiapi.Image()

#start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

j=1
while cv2.waitKey() != ord('q'):
    cam.get_image(img)
    image = img.get_image_data_numpy()
    image = cv2.resize(image,(240,240))
    cv2.imshow("test", image)
    cv2.waitKey(1)
    k = cv2.waitKey(0)
    if k == ord(" "):
        cv2.imwrite("test" + str(j) + ".png", image)
    j = j + 1
    if j==5:
        break
img1 = cv2.imread("test1.jpg")
img2 = cv2.imread("test2.jpg")
img3 = cv2.imread("test3.jpg")
img4 = cv2.imread("test4.jpg")

#Merged images
img1 = cv2.resize(img1, (240, 240))
img2 = cv2.resize(img2, (240, 240))
img3 = cv2.resize(img3, (240, 240))
img4 = cv2.resize(img4, (240, 240))

top_row = np.hstack((img1, img2))
low_row = np.hstack((img3, img4))

vis = np.vstack((top_row, low_row))

#Taking part of the image
part2 = vis[240:480, 0:240]
b1,g1,r1=cv2.split(part2)
B2 = np.empty((240, 240), dtype=b1.dtype)
R2 = np.empty((240, 240), dtype=r1.dtype)
G2 = np.empty((240, 240), dtype=g1.dtype)
cv2.imshow("druhy", part2)
for i in range(240):
    for ii in range(240):
        B2[ii,239-i]=b1[i,ii]
        R2[ii,239-i]=r1[i,ii]
        G2[ii,239-i]=g1[i,ii]
roto = cv2.merge([B2,G2,R2])
cv2.imshow("roto", roto)
vis[0:240, 0:240] = roto
cv2.imshow("merged", vis)

#Change all channels of BGR to 0 exept R
b1,g1,r1=cv2.split(vis)
cv2.imshow("cervik", b1)
merged = cv2.merge([b1*0, g1*0, r1*1])
cv2.imshow("merged2", merged)

#Convolution
kernel1 = np.array([[1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9]])

identity = cv2.filter2D(src=vis, ddepth=-1, kernel=kernel1)
cv2.imshow("identity", identity)

#Show parameters
print("sirka ", vis.shape[0])
print("vyska ", vis.shape[1])
print("pocet kanalov ", vis.shape[2])
cv2.waitKey(0)


# for i in range(10):
#     #get data and pass them from camera to img
#     cam.get_image(img)
#     image = img.get_image_data_numpy()
#     cv2.imshow("test", image)
#     cv2.waitKey()
#     #get raw data from camera
#     #for Python2.x function returns string
#     #for Python3.x function returns bytes
#     data_raw = img.get_image_data_raw()
#
#     #transform data to list
#     data = list(data_raw)
#
#     #print image data and metadata
#     print('Image number: ' + str(i))
#     print('Image width (pixels):  ' + str(img.width))
#     print('Image height (pixels): ' + str(img.height))
#     print('First 10 pixels: ' + str(data[:10]))
#     print('\n')

#stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

#stop communication
cam.close_device()

print('Done.')