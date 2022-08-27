import cv2
import numpy as np
import matplotlib.pyplot as plt

# Sobel Operator
'''
img = cv2.imread(r"images/double_edge.jpg",0)

# output data type = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)

# Output data type = cv2.CV_64F, Then take it's absolute and convert to cv2.CV_8U

sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
abs_sobel64f = cv2.convertScaleAbs(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)


plt.subplot(141)
plt.title("sobelx8u")
plt.imshow(sobelx8u,cmap="Greys_r")
plt.axis('off')

plt.subplot(142)
plt.title("sobelx64f")
plt.imshow(sobelx64f,cmap="Greys_r")
plt.axis('off')

plt.subplot(143)
plt.title("abs_sobel64f")
plt.imshow(abs_sobel64f,cmap="Greys_r")
plt.axis('off')

plt.subplot(144)
plt.title("sobel_8u")
plt.imshow(sobel_8u,cmap="Greys_r")
plt.axis('off')


plt.show()
'''


# Canny Edge Detection

'''

img_box = cv2.imread(r"images/double_edge.jpg",0)
img_tele = cv2.imread(r"images/telephone.jpg",0)
img_j = cv2.imread(r"images/j.png",0)

# edges_img= cv2.Canny(img,minThreshold,maxThreshold)

box_edges = cv2.Canny(img_box,100,200)
tele_edges = cv2.Canny(img_tele,100,200)
j_edges = cv2.Canny(img_j,100,200)


plt.subplot(321)
plt.title("box_Original")
plt.imshow(img_box,cmap="Greys_r")
plt.axis('off')

plt.subplot(322)
plt.title("box_edges")
plt.imshow(box_edges,cmap="Greys_r")
plt.axis('off')

plt.subplot(323)
plt.title("img_Original")
plt.imshow(img_tele,cmap="Greys_r")
plt.axis('off')

plt.subplot(324)
plt.title("tele_edges")
plt.imshow(tele_edges,cmap="Greys_r")
plt.axis('off')

plt.subplot(325)
plt.title("j_Original")
plt.imshow(img_j,cmap="Greys_r")
plt.axis('off')

plt.subplot(326)
plt.title("j_edges")
plt.imshow(j_edges,cmap="Greys_r")
plt.axis('off')

plt.show()

'''

# Laplacian Filter

'''

img = cv2.imread(r"images/sudoku-original_clahe.jpg",cv2.IMREAD_GRAYSCALE)

laplacian_8 = cv2.Laplacian(img,cv2.CV_8U,ksize=3)
laplacian_16 = cv2.Laplacian(img,cv2.CV_16U,ksize=3)

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(img,cmap="Greys_r")
plt.axis('off')

plt.subplot(1,3,2)
plt.title("laplacian_8")
plt.imshow(laplacian_8,cmap="Greys_r")
plt.axis('off')

plt.subplot(1,3,3)
plt.title("laplacian_16")
plt.imshow(laplacian_16,cmap="Greys_r")
plt.axis('off')

plt.show()

'''
