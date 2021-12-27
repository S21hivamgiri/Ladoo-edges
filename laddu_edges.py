#For Computer Visioning
import cv2
# For Image processing
from PIL import Image

#input image
input = "laddu.jpeg"
#output image
output = "output_laddu.jpeg"
#optimized image
optimized = "optimized_laddu.jpeg"

#display Input Image
input_img=Image.open(input)
input_img.show()

#Read input image
image = cv2.imread(input)

#Convert the image into gray shades
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Blur the gray Image to remove/whiten non significant part of image
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
#Convert the image into outline to get edges
canny = cv2.Canny(blurred, 30, 150)
#Finding all contours in aboyve image
contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#Inscribe contours on orignal image
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

#Display Output
cv2.imwrite(output, image)
Image.open(output)

#rerun the above steps for better edges for optimization 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
canny = cv2.Canny(blurred, 30, 90)
contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

#Display Optimized Output
cv2.imwrite(optimized, image)
Image.open(optimized)