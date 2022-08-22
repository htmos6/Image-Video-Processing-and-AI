# This script prevents open-cv kernel errors
import cv2
img = cv2.imread("path_to_opened_image")

while (True):
    cv2.imshow("Puppy", img)
    
    # if we have waited 1ms AND pressed ESC --> Exit
    if (cv2.waitKey(1) and 0xFF == 27):
       break
cv2.destroyAllWindows()
