import cv2

#for color image
img = cv2.imread('dog5.jpg', 1)

#for grayscale image
#img = cv2.imread('dog5.jpg', 0)

#for alpha channel image
#img = cv2.imread('dog5.jpg', -1)


print(img)

cv2.imshow('image', img)
k=cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('dog5_copy.png', img)
