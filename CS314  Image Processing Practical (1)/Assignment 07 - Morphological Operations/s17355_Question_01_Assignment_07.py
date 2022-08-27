import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread(r'images/overlap_coins.jpg',cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img_gray,50,255,0)



inverse_img = cv2.bitwise_not(thresh)


#rectangular kernel

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

erosion = cv2.erode(inverse_img,kernel,iterations=3)

erosion_copy_for_contours = erosion.copy()
erosion_copy_for_draw_contours = erosion.copy()
erosion_copy_for_draw_contours_perimeter = erosion.copy()

erosion_copy_for_draw_contours_BGR = cv2.cvtColor(erosion_copy_for_draw_contours,cv2.COLOR_GRAY2BGR)
erosion_copy_for_draw_contours_perimeter_BGR = cv2.cvtColor(erosion_copy_for_draw_contours_perimeter,cv2.COLOR_GRAY2BGR)



contours,hierarchy = cv2.findContours(erosion_copy_for_contours,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Question 01

# part a.  Number of coins available in the image
number_of_coins = len(contours)



# part b.  Total area covered by coins

resulting_contours_image = cv2.drawContours(erosion_copy_for_draw_contours_BGR,contours,-1,(0,255,0),2)


area = cv2.contourArea(contours[0])


# writing text

position = (20,20) # y,x

text = "# Coins area : " + str(area) + " pixel^2  # Number of Coins : " + str(number_of_coins)

cv2.putText(
    resulting_contours_image,
    text,
    position,
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (255,255,0,255),
    2
    )

#cv2.imshow("test",resulting_contours_image)


# part c. The perimeter of the 2nd to largest coin


sorted_contours = sorted(contours, key=cv2.contourArea , reverse=True)

perimeter = cv2.arcLength(sorted_contours[1],True)

perimeter = "{0:.2f}".format(perimeter)
position_perimeter = (6,10) # x,y
text_perimeter = "Square Perimeter : " + str(perimeter) + " pixels"

img2 = cv2.drawContours(erosion_copy_for_draw_contours_perimeter_BGR,sorted_contours[1],-1,(255,0,0),2)

#cv2.imshow("coin having the 2nd largest contour area ",img2)


plt.subplot(151)
plt.title("Original")
plt.imshow(img,cmap="Greys_r")
plt.axis('off')

plt.subplot(152)
plt.title("inverse_Binary_image")
plt.imshow(inverse_img,cmap="Greys_r")
plt.axis('off')

plt.subplot(153)
plt.title("eroded_image")
plt.imshow(erosion,cmap="Greys_r")
plt.axis('off')

plt.subplot(154)
plt.title("contours_image")
plt.imshow(resulting_contours_image,cmap="Greys_r")
plt.axis('off')

plt.subplot(155)
plt.title("Perimeter")
plt.text(15,20,text_perimeter,fontsize=8,color='r')
plt.imshow(img2,cmap="Greys_r")
plt.axis('off')


plt.show()







