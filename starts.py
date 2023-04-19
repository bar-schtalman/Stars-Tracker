import cv2
# Get image of stars
# Turn the image into file of coordinates x,y,r,b
# x,y - star's coordinate
# r - radius
# b - brightness of the star

import cv2
import numpy as np

# Load the image
img = cv2.imread('stars.jpeg')
print("line 13 ", img)

# Convert to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Set the threshold value
threshold = 150

# Threshold the image to isolate the stars
thresh = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)[1]

# Find the contours of the stars
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw circles around the stars
output_img = img.copy()
for i, contour in enumerate(contours):
    # Calculate the moments of the contour to determine centroid
    moments = cv2.moments(contour)
    if moments["m00"] == 0:
        continue
    x = int(moments["m10"] / moments["m00"])
    y = int(moments["m01"] / moments["m00"])

    # Calculate the radius of the contour
    (x, y), radius = cv2.minEnclosingCircle(contour)
    radius = int(radius)

    # Draw the circle
    cv2.circle(output_img, (int(x), int(y)), radius, (0, 0, 255), 2)

    # Calculate the brightness of the star
    mask = np.zeros_like(img)
    cv2.drawContours(mask, [contour], 0, (255, 255, 255), -1)
    mask = mask.astype(bool)
    brightness = np.mean(img[mask])

    # Print the results
    print(f"Star {i + 1}: x={x}, y={y}, radius={radius}, brightness={brightness:.2f}")

# Save the output image
cv2.imwrite('output.jpg', output_img)
# # Show the image with circles around the stars
# cv2.imshow("Stars", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()