import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageChops

# Load the image
image = Image.open('fr2.jpg')

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

# Save the resulting image
brightened_image.save('aftermain.jpg')