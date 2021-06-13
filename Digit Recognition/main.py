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
         