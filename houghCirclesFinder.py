# _---------------------------------------------------
# __name__          "Hough Circles Finder"
# __author__        "Dávid Szépvölgyi && Jakub Rabčan"
# __version__       "1.0.0"
# __maintainer__    "Dávid Szépvölgyi && Jakub Rabčan"
# __email__         "david.szepvolgyi@gmail.com"
# __status__        "Production"
# -----------------------------------------------------

from ximea import xiapi
import cv2
import numpy as np

# Function takes input from camera and do algoritm whitch finds circles on current frame/image
def startVideoFinding():
    ### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###

    # create instance for first connected camera
    cam = xiapi.Camera()

    # start communication
    # to open specific device, use:
    # cam.open_device_by_SN('41305651')
    # (open by serial number)
    print('Opening first camera...')
    cam.open_device()

    # settings
    cam.set_exposure(10000)
    cam.set_param('imgdataformat', 'XI_RGB32')
    cam.set_param('auto_wb', 1)
    print('Exposure was set to %i us' % cam.get_exposure())

    # create instance of Image to store image data and metadata
    img = xiapi.Image()

    # start data acquisition
    print('Starting data acquisition...')
    cam.start_acquisition()

    def nothing(x):
        pass

    # Create a black image, a window
    cv2.namedWindow('detected circles')
    # create trackbars for color change
    cv2.createTrackbar('param1', 'detected circles', 10, 300, nothing)
    cv2.createTrackbar('param2', 'detected circles', 10, 300, nothing)
    cv2.createTrackbar('dp', 'detected circles', 1, 300, nothing)
    cv2.createTrackbar('mindist', 'detected circles', 1, 300, nothing)
    cv2.createTrackbar('minRad', 'detected circles', 0, 300, nothing)
    cv2.createTrackbar('maxRad', 'detected circles', 0, 300, nothing)
    # create switch for ON/OFF functionality

    j = 1
    while cv2.waitKey(1) != ord('q'):
        cam.get_image(img)
        image = img.get_image_data_numpy()
        image = cv2.resize(image, (240, 240))
        cimg = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        param1Val = cv2.getTrackbarPos('param1', 'detected circles')
        param2Val = cv2.getTrackbarPos('param2', 'detected circles')
        dpVal = cv2.getTrackbarPos('dp', 'detected circles')
        mindisVal = cv2.getTrackbarPos('mindist', 'detected circles')
        minRadVal = cv2.getTrackbarPos('minRad', 'detected circles')
        maxRadVal = cv2.getTrackbarPos('maxRad', 'detected circles')
        circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dpVal, mindisVal, param1=param1Val, param2=param2Val,
                                   minRadius=minRadVal, maxRadius=maxRadVal)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            n=0
            for i in circles[0, :]:
                n+=1
                # draw the outer circle
                cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
                if n > 200:
                    break

        cv2.imshow('detected circles', cimg)

        cv2.waitKey(1)

    # stop data acquisition
    print('Stopping acquisition...')
    cam.stop_acquisition()

    # stop communication
    cam.close_device()

    print('Done.')
    cv2.destroyAllWindows()
