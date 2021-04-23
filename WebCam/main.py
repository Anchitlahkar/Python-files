import cv2
import time
import random, dropbox


def take_SnapShort():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while result:
        ret, frame = videoCaptureObject.read()
        imgName = 'img'+str(random.randint(0, 100))+'.png'
        cv2.imwrite(imgName, frame)
        startTime = time.time()
        result = False

        return imgName

    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(imgName):
        dbx = dropbox.Dropbox('yGNCqYxnD6QAAAAAAAAAAQxm9ZwFySM4SnlKYaE4_qW4v2TCtO3OibEsfmEZdWjR')

        with open(imgName, 'rb') as f:
            dbx.files_upload(f.read(), '/img/'+imgName)


def main():
    startTime = time.time()
    while True:
        if (time.time() - startTime) >= 60:
            name = take_SnapShort()
            upload_file(name)
            startTime = time.time()

main()
