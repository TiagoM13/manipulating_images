import cv2

img = cv2.imread('../img/image.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('../img/grayscaleimage.png', img)
