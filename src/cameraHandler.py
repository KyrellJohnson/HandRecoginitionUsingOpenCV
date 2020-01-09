import numpy as np
import cv2


def nothing(x):
    pass


# create camera element
cap = cv2.VideoCapture(0)

# Window for camera
cv2.namedWindow("frame")
# create trackbars for HSV values
cv2.namedWindow("Values", cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar("Hue LO", "Values", 108, 255, nothing)
cv2.createTrackbar("Sat LO", "Values", 23, 255, nothing)
cv2.createTrackbar("Value LO", "Values", 82, 255, nothing)
cv2.createTrackbar("Hue HI", "Values", 179, 255, nothing)
cv2.createTrackbar("Sat HI", "Values", 255, 255, nothing)
cv2.createTrackbar("Value HI", "Values", 255, 255, nothing)

while (True):
    # Capture frame-by-frame
    _, frame = cap.read()

    # let x = "hsv value" of trackbar
    Hue0 = cv2.getTrackbarPos("Hue LO", "Values")
    Sat0 = cv2.getTrackbarPos("Sat LO", "Values")
    Val0 = cv2.getTrackbarPos("Value LO", "Values")
    Hue1 = cv2.getTrackbarPos("Hue HI", "Values")
    Sat1 = cv2.getTrackbarPos("Sat HI", "Values")
    Val1 = cv2.getTrackbarPos("Value HI", "Values")

    # convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range (hsv) to mask
    lowerColor = np.array([Hue0, Sat0, Val0])
    upperColor = np.array([Hue1, Sat1, Val1])

    # create mask that only get hsv within threshold
    mask = cv2.inRange(hsv, lowerColor, upperColor)

    # result of the masking with color
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # erosion
    kernel = np.ones((5, 5), np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations=1)
    erosion = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("frame", frame)  # default color frame
    cv2.imshow("mask", mask)  # frame with mask component
    cv2.imshow("erosion", erosion)  # frame with mask component + noise reduction
    cv2.imshow("res", res)

    # stop program on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
