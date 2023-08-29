import cv2
import numpy as np

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cv2.namedWindow('cameras')
cv2.createTrackbar('minimum', 'cameras', 0, 255, lambda x: None)
cv2.createTrackbar('maximum', 'cameras', 0, 255, lambda x: None)

while True:
    st1, img1 = cam1.read()
    st2, img2 = cam2.read()

    if not st1 or not st2:
        print("Error reading frames from one or both cameras.")
        break

    # Resize the frames to have the same dimensions
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Horizontally stack the resized frames
    out = np.hstack((img1, img2_resized))

    min_val = cv2.getTrackbarPos('minimum', 'cameras')
    max_val = cv2.getTrackbarPos('maximum', 'cameras')
    outline = cv2.Canny(out, min_val, max_val, 3)  # Apply Canny edge detection
    cv2.imshow('cameras', outline)

    cv2.imshow("Camera 1", img1)
    cv2.imshow("Camera 2", img2_resized)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam1.release()
cam2.release()
cv2.destroyAllWindows()
