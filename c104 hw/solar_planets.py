import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20, 300), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "mercury",
            (120, 200), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "venus",
            (200, 200), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "earth",
            (280, 200), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mars",
            (390, 200), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "jupiter",
            (480, 200), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "saturn",
            (680, 200), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "uranus",
            (980, 150), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "neptune",
            (1080, 200), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname",img)
