import cv2
maxwidth, maxheight = 400, 500

img = cv2.imread('../img/image.jpeg')
f1 = maxwidth / img.shape[1]
f2 = maxheight / img.shape[0]
f = min(f1, f2)  # resizing factor
dim = (int(img.shape[1] * f), int(img.shape[0] * f))
resized = cv2.resize(img, dim)
cv2.imwrite('../img/rezidedimage.png', resized)
