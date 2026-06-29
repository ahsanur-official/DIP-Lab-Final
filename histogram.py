import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("image.png", 0)

# Show image
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")
plt.show()

# Histogram
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()
