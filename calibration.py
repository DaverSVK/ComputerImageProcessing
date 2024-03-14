#_---------------------------------------------------
# __name__          "Camera Calibration"
# __author__        "Dávid Szépvölgyi && Jakub Rabčan"
# __version__       "1.0.0"
# __maintainer__    "Dávid Szépvölgyi && Jakub Rabčan"
# __email__         "david.szepvolgyi@gmail.com"
# __status__        "Production"
#-----------------------------------------------------

from ximea import xiapi
import cv2
import numpy as np
import glob



#Function takes nOfPicks and will store them in "Recources/" as input it needs int number
def makeCameraPictures(nOfPics):
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
            cv2.imwrite("Recources/test" + str(j) + ".jpeg", image)
        j = j + 1
        if j==nOfPics:
            break

    #stop data acquisition
    print('Stopping acquisition...')
    cam.stop_acquisition()

    #stop communication
    cam.close_device()

    print('Done.')

def calibrateTheCameraUsingUdistortion():
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((5*7,3), np.float32)
    objp[:,:2] = np.mgrid[0:7,0:5].T.reshape(-1,2)
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    images = glob.glob('Recources/*.jpg')
    u = 0
    for fname in images:
        u +=1
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (7,5), None)
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)
            # Draw and display the corners
            cv2.drawChessboardCorners(img, (7,5), corners2, ret)
            cv2.imshow('img'+ str(u) , img)
            cv2.waitKey(0)
    cv2.destroyAllWindows()

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    img = cv2.imread('test5 .jpeg')
    h,  w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite('calibresult.png', dst)

    # undistort
    mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
    dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite('calibresult2.png', dst)

    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        mean_error += error
    print( "total error: {}".format(mean_error/len(objpoints)) )
    #
