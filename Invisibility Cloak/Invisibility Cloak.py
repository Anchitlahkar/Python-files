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

    #Generating mask to detect red colour

    lower_red = np.array([0,120,50])
    upper_red = np.array([10,255,255])

    mask_1 = cv2.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([170,120,50])
    upper_red = np.array([180,255,255])

    mask_2 = cv2.inRange(hsv,lower_red,upper_red)

    mask_1 = mask_1+mask_2

    #Open and expand the image where there is mask 1 (color)
    # Syntax: morphologyEx(src, dst, op, kernel)
    # morphologyEx() is the method of the class Img Processing which is used to perform operations on a given image
    # MORPH_OPEN and MORPH_DILATE

    mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    # we need to create  a mask to segment out the red color from the frame
    # we use bitwise_not() method

    #Selecting only the part that does not have mask one and saving in mask 2

    mask_2 = cv2.bitwise_not(mask_1)

    # we need to create 2 resolutions
    # first- image without color red
    # second - background from background image we captured earlier
    # combined - will give u the output

    #Keeping only the part of the images without the red color 

    res_1 = cv2.bitwise_and(img,img,mask=mask_2)

    #Keeping only the part of the images with the red color

    res_2 = cv2.bitwise_and(bg,bg,mask=mask_1)

    #Generating the final output by merging res_1 and res_2

    final_output = cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(final_output)

    #Displaying the output to the user
    cv2.imshow("magic", final_output)
    cv2.waitKey(1)


capture.release()
output_file.release()
cv2.destroyAllWindows()

