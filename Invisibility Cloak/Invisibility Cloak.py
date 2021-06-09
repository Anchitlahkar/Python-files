import cv2
import time
import numpy as np

"""
 1. Capture and store the background frame. [ This will be done for some seconds ]
 2. Detect the red colored cloth using color detection and segmentation algorithm
 3. Segment out the red colored cloth by generating a mask. [ used in code ]
 4. Generate the final augmented output to create a magical effect. [ video.mp4 ]
"""

# to save the output in a file -'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# starting the webcam
capture = cv2.VideoCapture(0)

# allowing the webcam to warm up
time.sleep(2)

# capturing background for 60 frames 
bg = 0

for i in range(0, 60):
    ret, bg = capture.read()

# fliping the background
bg = np.flip(bg, axis=1)

# reading the caputered frame untill the camare is open
while capture.isOpened():
    ret, img = capture.read()

    if not ret:
        break
    
    # fliping the img
    img = np.flip(img, axis=1)

    # converting the color from bgr to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


