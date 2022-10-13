import cv2
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
vc = cv2.VideoCapture('cxk.mp4')
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

c = 1
while rval:
    rval, frame = vc.read()
    if rval == False:
        break
    frame = imageToChar(frame)
    cv2.imwrite('./images/' + str(c) + '.jpg', frame)
    print(c)
    c = c + 1
    cv2.waitKey(1)
vc.release()
