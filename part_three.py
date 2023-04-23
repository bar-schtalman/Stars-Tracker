import sys
import cv2
import numpy as np

# Get the image filenames from command line arguments
# run it this way:
# py part_three.py image1.jpg image2.jpg
img1_filename = sys.argv[1]
img2_filename = sys.argv[2]

# Gets two images and turn them gray
img1 = cv2.imread(img1_filename, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_filename, cv2.IMREAD_GRAYSCALE)


# Creates a Scale-Invariant Feature Transform (SIFT) object
sift = cv2.SIFT_create()

# Use SIFT's function to detect key-points and compute their descriptors in an image.
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Uses the FLANN (Fast Library for Approximate Nearest Neighbors) algorithm to perform the feature matching
matcher = cv2.FlannBasedMatcher()

# Using the KNN method we get a list of matches, where each match
# is represented by a pair of object which contains information about the
# distance between the descriptors of the two key-points ((x,y) location)
# and their indices in the descriptor arrays.
#
# The knnMatch method takes three arguments: descriptor, a second descriptor, and some k.
#       First & second descriptors are the key-points in the two images we want to match
#       K - return the best matches (2 in our case) for each keypoint in the first descriptor
matches = matcher.knnMatch(des1, des2, k=2)

# Declare & init a list of matches:
good_matches = []

# Only apply the good matches but not every matches
for o, p in matches:
    if o.distance < 0.75*p.distance:
        good_matches.append(o)

# Coordinates of the (x,y) location that correspond to be considered as a match:
# reshape (x, y, z)
# x - "infer the remaining dimensions",
# y - "insert a new dimension at position y",
# z - "each element has two components".
points1 = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
points2 = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# Put each photo to next one and mark the matches with lines
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None)

# Output the matches
cv2.imwrite('output_matches.jpg', img_matches)

# Prints amount of good matches
print('Amount of matches:', len(good_matches))

# Write the matches into CSV file
with open('matches.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x1', 'y1', 'x2', 'y2'])
    for i in range(len(good_matches)):
        writer.writerow([points1[i][0][0], points1[i][0][1], points2[i][0][0], points2[i][0][1]])
