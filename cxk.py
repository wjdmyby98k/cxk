import cv2
import numpy as np


def readVideo(path):
    videoCapture = cv2.VideoCapture()
    videoCapture.open(path)
    f = videoCapture.get(5)
    fps = videoCapture.get(7)
    print(f,fps)
    while (True):
        ret, frame = videoCapture.read()
        # ret是bool类型，frame是image ndarray类型
        src = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))
        src = imageToChar(src)
        cv2.imshow('frame', src)
        cv2.waitKey(1)
    cv2.destroyAllWindows()


def imageToChar(img):
    string = "qwertyuiopasdfghjjklzxcvbnmcxkcxkcxckxkccxk"
    count = len(string)
    u, v, _ = img.shape
    c = img * 0 + 0
    # c = np.zeros((u,v))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('output', c)
    for i in range(0, u - 1, 10):
        for j in range(0, v - 1, 10):
            pix = gray[i, j]
            b, g, r = img[i, j]
            zifu = string[int(((count - 1) * pix) / 256)]
            cv2.putText(c, zifu, (j, i), cv2.FONT_HERSHEY_COMPLEX, 0.5, (int(255), int(255), int(255)))
    return c


readVideo('cxk.mp4')
cv2.waitKey(0)
