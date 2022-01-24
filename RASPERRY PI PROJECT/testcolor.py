# Importing all modules
import cv2
import numpy as np

# Specifying upper and lower ranges of color to detect in hsv format

#lower_yellow = np.array([15, 150, 20])
#upper_yellow = np.array([35, 255, 255]) # (These ranges will detect Yellow)

lower_red = np.array([175, 150, 20])
upper_red = np.array([180, 255, 255])#(These ranges will detect red)

lower_green = np.array([35, 150, 20])
upper_green = np.array([75, 255, 255])#(These ranges will detect green)

lower_orange = np.array([5, 50, 20])
upper_orange = np.array([15, 255, 255])#(These ranges will detect orange)

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)

while True:
    success, video = webcam_video.read() # Reading webcam footage

    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format

    mask_red = cv2.inRange(img, lower_red, upper_red) # Masking the image to find our color
    mask_orange = cv2.inRange(img, lower_orange, upper_orange)
    mask_green = cv2.inRange(img, upper_green, upper_green)

    
    mask_contours_r, hierarchy = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask_contours_o, hierarchy = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask_contours_g, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image

    # Finding position of all red contours
    if len(mask_contours_r) != 0:
        for mask_contour in mask_contours_r:
            if cv2.contourArea(mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle
              

    cv2.imshow("Color Detection", mask_red) # Displaying mask image

    cv2.imshow("window", video) # Displaying webcam image

    cv2.waitKey(1)

        

    
    