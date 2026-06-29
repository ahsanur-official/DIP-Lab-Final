import cv2

# Read two images
img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

# Resize if needed
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Addition
add = cv2.add(img1, img2)

# Subtraction
sub = cv2.subtract(img1, img2)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Addition", add)
cv2.imshow("Subtraction", sub)

cv2.waitKey(0)
cv2.destroyAllWindows()
