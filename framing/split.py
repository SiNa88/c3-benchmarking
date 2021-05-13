import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('20-200.mp4')

try:
    if not os.path.exists('data-20-200'):
        os.makedirs('data-20-200')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret: break
    # Saves image of the current frame in jpg file
    name = './data-20-200/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    #print(ret)
    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
