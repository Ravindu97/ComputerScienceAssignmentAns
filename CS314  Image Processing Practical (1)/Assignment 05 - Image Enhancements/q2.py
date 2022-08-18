import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(r"1.jpg",cv2.IMREAD_COLOR)


def clahe(image,limit):

    h,s,v = cv2.split(cv2.cvtColor(image,cv2.COLOR_BGR2HSV))
    
    # Creating a CLAHE Object

    clahe = cv2.createCLAHE(clipLimit=limit,tileGridSize=(8,8))
    color_value_clahe = clahe.apply(v)

    # mergeing

    final_image = cv2.merge([h,s,color_value_clahe])
    bgr_final_image = cv2.cvtColor(final_image,cv2.COLOR_HSV2BGR)
    return bgr_final_image



clip_limit_value = [2.0,5.0,10.0,20.0]
labels = ["2.0","5.0","10.0","20.0"]


for i in range(len(clip_limit_value)):
    plt.subplot(1,4,i+1)
    plt.imshow(clahe(img,clip_limit_value[i]))
    plt.title("limit : " + labels[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
