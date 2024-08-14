import cv2

# destroy all window open images in one key press
# img= cv2.imread("images.jpeg")
# cv2.imshow("bakri image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# destroy specific window imaage on key press
img= cv2.imread("images.jpeg")
cv2.imshow("demo image",img)
cv2.imshow("demo image1",img)
cv2.waitKey(0)
cv2.destroyWindow("demo image1")
