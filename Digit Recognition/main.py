import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import frame
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps

X, y = fetch_openml("mnist_784", version=1, return_X_y=True)


print(pd.Series(y).value_counts())

classes = ['0','1','2','3','4','5','6','7','8','9']
len_Classes = len(classes)


# Spliting The Data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, train_size=7500, test_size=2500)

X_train_scaled = X_train/255.0
X_test_scaled = X_test/255.0

classifier = LogisticRegression(solver='saga', multi_class='multinomial')
classifier.fit(X_train_scaled, y_train)


# Prediction  
y_prediction = classifier.predict(X_test_scaled)

# Accuracy Score
accuracy = accuracy_score(y_test, y_prediction)
print(accuracy)

"""
Here we'll use the try except block as try block lets us test the code for errors and except block lets us handle the errors.
The try except block has 2 blocks. 1st try where you write the code which you want to execute.
2nd except block which catches the errors from the try block .
"""

capture = cv2.VideoCapture(0)

while True:
    try:
        ret, frm = capture.read()

        # converting the frame into grey color
        grey = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

        # Drawing a box in the center of the Video
        height, width = grey.shape

        upper_left = (int(width/2-56), int(height/2-56))
        bottom_right = (int(width/2+56), int(height/2+56))

        cv2.rectangle(grey, upper_left, bottom_right, (0,255,0), 2)


        # to only consider the area inside the box for detecting the digit           roi(region of interest)
        roi = grey[upper_left[1]:bottom_right[1], upper_left[0]: bottom_right[0]]

        print('2st Part')
        
        # converting cv2 img to PIL(Python Image Lib)
        img_pil = Image.fromarray(roi)

        img_bw = img_pil.convert('L')

        img_resized = img_bw.resize((28,28), Image.ANTIALIAS)

        # import the img
        img_inverted = PIL.ImageOps.invert(img_resized)

        pixel_filter = 20

        print('3st Part')

        # converting to scaler quantity
        min_pixel = np.percentile(img_inverted, pixel_filter)
        img_scaled = np.clip(img_inverted - min_pixel, 0, 255)
        max_pixel = np.max(img_inverted)

        # converting into an array
        img_final = np.asarray(img_scaled)/max_pixel

        # create a test sample and make a prediction
        test_sample = np.array(img_scaled).reshape(1, 784)

        test_prediction = classifier.predict(test_sample)

        print('Prediction: ',test_prediction)

        cv2.imshow('Frame', grey)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    
    except Exception as e:
        pass

capture.release()
cv2.destroyAllWindows()
