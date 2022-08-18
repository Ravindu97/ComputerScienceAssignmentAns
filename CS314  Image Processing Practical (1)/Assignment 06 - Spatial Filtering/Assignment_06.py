import cv2
import numpy as np
import matplotlib.pyplot as plt

# Question 01

img = cv2.imread(r'circle.png',cv2.IMREAD_GRAYSCALE)

#cv2.imshow("test",img)

kernel_h = np.array([[1,1,1],
                     [1,1,1],
                     [1,1,1]])/9

#print(type(kernel_h))
#<class 'numpy.ndarray'>

#print(type(kernel_h[0,0]))
#<class 'numpy.float64'>

#   Examine the matrix h. Comment on the values and data type ?
#   Data typeof the kernel is a numpy ndarray having float64 valued numbers to represent equal weights to all pixels within the neighbourhood.

#   Why should the size of the kernel be odd?

'''
For an odd-sized filter, all the previous layer pixels would be symmetrical around the output pixel.
Without this symmetry, we will have to account for distortions across the layers.
'''

# Question 02

'''

mean_img_1 = cv2.filter2D(img,-1,kernel_h)

plt.subplot(421)
plt.title("Original\nGreys_colorMap")
plt.imshow(img,cmap="Greys_r")
plt.axis('off')

plt.subplot(422)
plt.title("Filtered\nGreys_colorMap")
plt.imshow(mean_img_1,cmap="Greys_r")
plt.axis('off')

plt.subplot(423)
plt.title("Original\njet_colorMap")
plt.imshow(img,cmap="jet")
plt.axis('off')

plt.subplot(424)
plt.title("Filtered\njet_colorMap")
plt.imshow(mean_img_1,cmap="jet")
plt.axis('off')

plt.subplot(425)
plt.title("Original\npink_colorMap")
plt.imshow(img,cmap="pink")
plt.axis('off')

plt.subplot(426)
plt.title("Filtered\npink_colorMap")
plt.imshow(mean_img_1,cmap="pink")
plt.axis('off')

plt.subplot(427)
plt.title("Original\nhot_colorMap")
plt.imshow(img,cmap="hot")
plt.axis('off')

plt.subplot(428)
plt.title("Filtered\nhot_colorMap")
plt.imshow(mean_img_1,cmap="hot")
plt.axis('off')

plt.show()

'''

# Question 03

# Previous Question we have used custom kernel, same can be achived using built in averaging_filters

'''

blur_box_filter_5x5 = cv2.boxFilter(img,-1,(5,5))

blur_box_filter_15x15  = cv2.boxFilter(img,-1,(15,15))

# when the kernel size increases bluring effect increases, hence noise will further be reduced

plt.subplot(131)
plt.title("Original")
plt.imshow(img,cmap="Greys_r")
plt.axis('off')

plt.subplot(132)
plt.title("Kernel 5x5")
plt.imshow(blur_box_filter_5x5,cmap="Greys_r")
plt.axis('off')

plt.subplot(133)
plt.title("Kernel 15x15")
plt.imshow(blur_box_filter_15x15,cmap="Greys_r")
plt.axis('off')

plt.show()

'''

# Question 04 Mean vs Median filter

#Median blur is better to remove salt and pepper noise

'''

Mean_filter_ker_5 = cv2.boxFilter(img,-1,(5,5))
median_filter_ker_5 = cv2.medianBlur(img,5)

plt.subplot(131)
plt.title("Original")
plt.imshow(img,cmap="Greys_r")
plt.axis('off')

plt.subplot(132)
plt.title("Mean_filter")
plt.imshow(Mean_filter_ker_5,cmap="Greys_r")
plt.axis('off')

plt.subplot(133)
plt.title("Median_filter")
plt.imshow(median_filter_ker_5,cmap="Greys_r")
plt.axis('off')

plt.show()

'''

# Question 05 Effect of increasing kernel size of median filters


'''
 the median filter has a low pass behavior, that is, it tends to smooth the image.
 And the cutoff frequency decreases with the increase in the size of the kernel.
 So, a large kernel means the sharpness of the image is lost.
'''


''''

median_filter_ker_5 = cv2.medianBlur(img,5)
median_filter_ker_15 = cv2.medianBlur(img,15)

plt.subplot(131)
plt.title("Original")
plt.imshow(img,cmap="Greys_r")
plt.axis('off')

plt.subplot(132)
plt.title("Median_filter\nKer_5")
plt.imshow(median_filter_ker_5,cmap="Greys_r")
plt.axis('off')

plt.subplot(133)
plt.title("Median_filter\nKer_5")
plt.imshow(median_filter_ker_15,cmap="Greys_r")
plt.axis('off')

plt.show()


'''
