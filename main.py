from calibration import *
from houghCirclesFinder import *

MACRO_CALIBRATION = True

# Calibration
if MACRO_CALIBRATION:
    # makeCameraPictures(20)
    calibrateTheCameraUsingUdistortion()

else:
    # Hough Circles
    startVideoFinding()



