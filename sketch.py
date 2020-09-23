import cv2
#Get location
img_location = 'C:/Users/c.san.emeterio/Desktop/aca/Docs/'
filename = 'face.png'
#read image
img = cv2.imread(img_location+filename)

#convert to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

#invert image
invert_gray_image = 250 - gray_image

#Blur image
blurred_img = cv2.GaussianBlur(invert_gray_image, (31,31), 0)

#invert blurred image
invert_blurred_img = 250 - blurred_img

#pencil sketch
pencil_sketch_IMG = cv2.divide(gray_image, invert_blurred_img, scale=256.0)

#show image
# cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_IMG)
cv2.waitKey(0)