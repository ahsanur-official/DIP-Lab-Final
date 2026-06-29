import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread("image.png")
img2 = cv2.imread("image2.png")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
g = img1.astype(int) + img2.astype(int)

g = np.clip(g, 0, 255).astype(np.uint8)

crimg = g
img = cv2.cvtColor(crimg, cv2.COLOR_BGR2GRAY)
l = 256
hist = np.zeros(l)
for p in img.flatten():
    hist[p] += 1

cdf = np.cumsum(hist / img.size)
equilize = np.round((l - 1) * cdf).astype(np.uint8)[img]

plt.figure(figsize=[12, 8])
plt.subplot(232)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.subplot(233)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.subplot(234)
plt.imshow(cv2.cvtColor(crimg, cv2.COLOR_BGR2RGB))
plt.subplot(235)
plt.hist(img.flatten(), 256)
plt.subplot(236)
plt.hist(equilize.flatten(), 256)
plt.tight_layout()
plt.show()
