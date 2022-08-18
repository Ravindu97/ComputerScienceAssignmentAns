import cv2
import numpy as np

# Read the image

img = cv2.imread("ColorChecker.png",cv2.IMREAD_COLOR)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# dictionary with the color as keys and HSV ranges

dict = {"blue":((80,100),(100,130)), "red":((0,5),(175,180)),"green":((45,50),(50,70)), "yellow":((20,30),(30,45)), "orange":((12,15),(15,20)), "purple":((130,150),(150,165)), "grey":((130,150),(150,165))}


# getting the user input

print("Available color Options:")
print(dict.keys())



def detect_colors(color):

    for key in dict.keys():

        if(color.casefold() == key.casefold()):

            if(color.lower() == "grey"):
               ## Generate grey value require to change the saturation values
                mask1 = cv2.inRange(img_hsv, (0,0,50), (0,0,240))
                mask2 = cv2.inRange(img_hsv, (0,0,50), (0,0,240))

            else:

                lower,upper = dict[color.lower()]
            
                ## Gen lower mask (0-5) and upper mask (175-180) for red (for example)
                mask1 = cv2.inRange(img_hsv, (lower[0],50,20), (lower[1],255,255))
                mask2 = cv2.inRange(img_hsv, (upper[0],50,20), (upper[1],255,255))


            ## Merge the mask and crop the red regions
            mask = cv2.bitwise_or(mask1, mask2 )
            croped = cv2.bitwise_and(img, img, mask=mask)

            ## Display
            cv2.imshow("mask", mask)
            cv2.imshow("croped", croped)

    



choice = input("Input the color you want to detect : ")

detect_colors(choice)






        
        













