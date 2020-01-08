import numpy as np
import cv2

def nothing(x):
    pass

#create camera element
cap = cv2.VideoCapture(0)

#create trackbars
cv2.namedWindow("frame")
cv2.createTrackbar("test", "frame", 50, 500, nothing)
cv2.createTrackbar("color/gray", "frame", 0, 1, nothing)


while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    test = cv2.getTrackbarPos("test", "frame")
    font = cv2.FONT_HERSHEY_COMPLEX
   # cv2.putText(frame, str(test), (50, 150), font, 4, (0, 0, 255))
    s = cv2.getTrackbarPos("color/gray", "frame")
    if s == 0:
        pass
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()