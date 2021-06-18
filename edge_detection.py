import cv2 as cv
import numpy as np

img = cv.imread('img/manohar.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edge = cv.Canny(gray, 0, 250)

# cv.imshow('gray', gray)
cv.imshow('edges', edge)
cv.imshow('orginal', img)

cv.waitKey(0)