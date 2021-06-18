import cv2 
import numpy as np

img = cv2.imread('img/luffy.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_inv = 255 - img_gray
img_blur = cv2.GaussianBlur(img_gray_inv, (11, 11), sigmaX=0, sigmaY=0)

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

final_img = dodgeV2(img_gray, img_blur)

cv2.imshow('final image', final_img)
cv2.imshow('orginal img', img)

cv2.waitKey(0)
