import cv2
import numpy as np

# Load the image
img = cv2.imread('star_hubble.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Set the threshold value
threshold = 100

# Threshold the image to isolate the stars
thresh = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)[1]

# Detect circles using HoughCircles
circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=1, minRadius=1, maxRadius=5)

# Draw circles around the stars
output_img = img.copy()
for i, circle in enumerate(circles[0, :]):
    x, y, radius = circle.astype(int)

    # Draw the circle
    cv2.circle(output_img, (x, y), radius, (0, 0, 255), 2)

    # Calculate the brightness of the star
    mask = np.zeros_like(img)
    cv2.circle(mask, (x, y), radius, (255, 255, 255), -1)
    mask = mask.astype(bool)
    brightness = np.mean(img[mask])

    # Print the results
    print(f"Star {i + 1}: x={x}, y={y}, radius={radius}, brightness={brightness:.2f}")

# Save the output image
cv2.imwrite('output.jpg', output_img)
