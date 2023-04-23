import io
import csv
from PIL import Image, ImageFilter, ImageChops
import cv2
import numpy as np
import argparse

import sys

# Read the image from stdin
parser = argparse.ArgumentParser(description='Process an image file')
parser.add_argument('file_path', metavar='FILE', help='the path to the image file')

# Parse the command-line arguments
args = parser.parse_args()

# Open the image file using PIL
image = Image.open(args.file_path)

# Convert the image to grayscale
gray_image = image.convert("L")

# Apply a threshold to the image
threshold = 175
thresholded_image = gray_image.point(lambda x: 255 if x > threshold else 0)

# Apply a Gaussian blur to the image
blurred_image = thresholded_image.filter(ImageFilter.GaussianBlur(radius=5))

# Create a mask for the stars
mask = ImageChops.invert(thresholded_image)

# Enhance the brightness of the stars
brightened_image = ImageChops.multiply(blurred_image, mask).point(lambda x: x * 3)

# Convert the PIL image to a numpy array
np_image = np.array(brightened_image)

# Convert the color format to BGR (for OpenCV compatibility)
bgr_image = cv2.cvtColor(np_image, cv2.COLOR_GRAY2BGR)

# Find contours in the brightened image
contours, hierarchy = cv2.findContours(np_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over each contour and calculate the center, brightness, and radius of each star
stars = []
for contour in contours:
    # Calculate the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Calculate the center of the contour
    cx = x + w/2
    cy = y + h/2

    # Calculate the brightness of the contour
    brightness = np.mean(np_image[y:y+h, x:x+w])

    # Calculate the radius of the contour
    radius = (w + h)/4

    # Append the x,y coordinates, brightness, and radius to the stars list
    stars.append({'x': cx, 'y': cy, 'brightness': brightness, 'radius': radius})

    # Draw a rectangle around the contour
    cv2.rectangle(bgr_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save the resulting image
result_image = Image.fromarray(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))
result_image.save('aftermain.jpg')

# Save the star data to a CSV file
with open('star_data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['star_number', 'x', 'y', 'brightness', 'radius']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for i, star in enumerate(stars):
        writer.writerow({'star_number': i+1, 'x': star['x'], 'y': star['y'], 'brightness': star['brightness'], 'radius': star['radius']})

# Print the number of stars
print("Number of stars: {}".format(len(stars)))