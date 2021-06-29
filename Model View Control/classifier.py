import numpy as np
import pandas as pd
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

dataset = np.load("image.npz")["arr_0"]

X = dataset
y = pd.read_csv("labels.csv")["labels"]

classes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
len_Classes = len(classes)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, test_size=0.25)

X_train_scaled = X_train/255.0
X_test_scaled = X_test/255.0


classifier = LogisticRegression(solver='saga', multi_class='multinomial')
classifier.fit(X_train_scaled, y_train)

y_prediction = classifier.predict(X_test_scaled)


def get_prediction(img):
    img_PIL = Image.open(img)

    img_bw = img_PIL.convert('L')
    img_resize = img_bw.resize((28, 28), Image.ANTIALIAS)

    pixcel_filter = 20
    min_pixcel = np.percentile(img_resize, pixcel_filter)

    img_scale = np.clip(img_resize - min_pixcel, 0, 255)
    max_pixcel = np.max(img_resize)

    img_resize_scaled = np.asarray(img_scale)/max_pixcel

    test_sample = np.array(img_resize_scaled).reshape(1, 784)
    test_prediction = classifier.predict(test_sample)

    return test_prediction[0]

