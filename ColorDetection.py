import cv2

import numpy as np
video_capture = cv2.VideoCapture(0)
print("color Detection running")
while True:

    rent, frames = video_capture.read()
    hsv_frame=cv2.cvtColor(frames,cv2.COLOR_BGR2HSV)

    #locate center of frame

    height,width,_=frames.shape
    centerX=int(width/2)
    centerY=int(height/2)
    pixel_center=hsv_frame[centerY,centerX]
    hue_value=pixel_center[0]  
    saturation = pixel_center[1]
    value= pixel_center[2]

    color ="undefined"
    if saturation < 50 and value > 200:
        color = "WHITE"
    elif hue_value < 100 and saturation < 100 and value < 100:
        color = "BLACK"
    elif hue_value < 10 or hue_value > 179:
        color = "RED"
    elif hue_value < 20:
        color = "ORANGE"
    elif hue_value < 24:
        color = "GOLD"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 60:
        color = "GREEN"
    elif hue_value < 80:
        color = "SPRING GREEN"
    elif hue_value < 100:
        color = "CYAN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 143:
        color = "VIOLET"
    elif hue_value < 146:
        color = "PURPLE"
    elif hue_value < 164:
        color = "PINK"
    elif hue_value < 170:
        color = "PINK"
    else:
        color = "RED"

    pixel_center_bgr=frames[centerY,centerX]
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    cv2.putText(frames, color, (centerX-300,centerY-200), 0, 1, (b, g, r), 3)
    cv2.circle(frames,(centerX,centerY),10,(b,g,r),3)

    cv2.imshow("Color Detection", frames)

 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
