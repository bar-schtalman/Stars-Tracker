import cv2
import numpy as np

# 1. Preprocess the images
img1 = cv2.imread('fr1.jpg')
img2 = cv2.imread('fr2.jpg')
img1 = cv2.resize(img1, (640, 480)) # resize the images to the same dimensions
img2 = cv2.resize(img2, (640, 480))
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # convert them to grayscale
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (5, 5), 0) # apply filters to enhance visibility
gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)

# 2. Detect features in each image
orb = cv2.ORB_create() # create ORB feature detector
kp1, des1 = orb.detectAndCompute(gray1, None) # detect keypoints and compute descriptors for img1
kp2, des2 = orb.detectAndCompute(gray2, None) # detect keypoints and compute descriptors for img2

# 3. Match features between the two images
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) # create Brute-Force Matcher
matches = bf.match(des1, des2) # match descriptors between img1 and img2
matches = sorted(matches, key = lambda x:x.distance) # sort the matches by distance

# 4. Geometric verification
good_matches = []
for m in matches:
    if m.distance < 0.7 * matches[0].distance: # apply Lowe's ratio test to filter out false matches
        good_matches.append(m)

M = None
if len(good_matches) > 10: # check if enough good matches are found
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0) # estimate the homography matrix using RANSAC
    matches_mask = mask.ravel().tolist()
else:
    print("Not enough good matches are found")

# 5. Visualize the matches
h, w = gray1.shape
if M is not None:
    pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)
    img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
    draw_params = dict(matchColor=(0, 255, 0), singlePointColor=None, matchesMask=matches_mask, flags=2)
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, **draw_params)
    cv2.imshow("Matches", img3)
else:
    cv2.imshow("Matches", img2)

cv2.waitKey(0)

