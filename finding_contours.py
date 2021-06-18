import cv2 as cv

img = cv.imread('img/rose.jpg')

blur = cv.GaussianBlur(img, (7,7), sigmaX=0, sigmaY=0)

img_gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 20, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

img_copy = img.copy()
cv.drawContours(image=img_copy, contours=contours, contourIdx=-1, color=(250, 150, 0), thickness=2, lineType=cv.LINE_AA)

cv.imshow('img', thresh)

cv.imshow('None approximation', img_copy)
cv.waitKey(0)
cv.imwrite('contours_none_image1.jpg', img_copy)
cv.destroyAllWindows()



