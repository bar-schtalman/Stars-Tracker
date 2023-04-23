import cv2
import numpy as np

# Load the two images
img1 = cv2.imread('fr1.jpg')
img2 = cv2.imread('fr2.jpg')

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create an ORB object
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors for both images
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Create a BFMatcher object
bf = cv2.BFMatcher()

# Match the descriptors using the BFMatcher
matches = bf.knnMatch(des1, des2, k=2)

# Apply Lowe's ratio test to select the best matches
good_matches = []
for m, n in matches:
    if m.distance < 0.80 * n.distance:
        good_matches.append(m)

# Draw the top 10 matches between the images
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches[:10], None)

# Resize the image to a specific width and height
width = 800
height = 600
img_matches_resized = cv2.resize(img_matches, (width, height))

# Save the output image
cv2.imwrite('xxxxxxx.jpg', img_matches_resized)
