import csv
from PIL import Image, ImageFilter, ImageChops
import cv2
import numpy as np
import argparse


"""
This is a part where using the terminal you upload a photo by writing the following command :
python main.py img.png 
* img.png is the name of the image you wish you upload *

More information about this code : 
This code plots a csv which writes the coordinates x y and r b , which r is the radiou and b is the brightness 
"""
parser = argparse.ArgumentParser(description='Process an image file')
parser.add_argument('file_path', metavar='FILE', help='the path to the image file')
args = parser.parse_args()
image = Image.open(args.file_path)

"""
Using PIL library, it will transfer the image into grascale. L is the mode of grayscale.
"""
gray_image = image.convert("L")

"""
Used threshold 175 on grayscale image, we tried more and less , but it worked the best with 175
each pixel above 175 automaticly will be set to 255
"""
threshold = 175
thresholded_image = gray_image.point(lambda x: 255 if x > threshold else 0)

"""
Linear filter that smooths an image by averaging the pixel values in the neightborhood of each pixel.
"""
blurred_image = thresholded_image.filter(ImageFilter.GaussianBlur(radius=5))

"""
Function from PIL library , and it inverts the colors of an image. It inverts which means each pixel that was 255
will be 0 now and the oposite.
"""
mask = ImageChops.invert(thresholded_image)

"""
Resulting image will be brighter regions where the features are more pronounced.
"""
brightened_image = ImageChops.multiply(blurred_image, mask).point(lambda x: x * 3)

"""
Converts the image object to NumPy array.
"""
np_image = np.array(brightened_image)

"""
Converts the image color from gray to bgr
"""
bgr_image = cv2.cvtColor(np_image, cv2.COLOR_GRAY2BGR)

"""
Function that helps to find contours in a binary image.
return coordinates x,y of the object points
"""
contours, hierarchy = cv2.findContours(np_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

"""
Loop over the contours and draw rectangels in coordinates x y w h
"""
stars = []
for contour in contours:
    # Calculate the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)

    """
    center of the contour
    """
    cx = x + w/2
    cy = y + h/2

    """
    brightness of the contour
    """
    brightness = np.mean(np_image[y:y+h, x:x+w])

    """
    radious of the contour
    """
    radius = (w + h)/4

    """
    appends to array stars 
    """
    stars.append({'x': cx, 'y': cy, 'brightness': brightness, 'radius': radius})

    """
    draws the rectangle
    """
    cv2.rectangle(bgr_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

"""
Saves the image after all the manipulations
"""
result_image = Image.fromarray(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))
result_image.save('aftermain1.jpg')

"""
Saves in a csv all the output x y brightness and radius
"""
with open('star_data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['star_number', 'x', 'y', 'brightness', 'radius']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for i, star in enumerate(stars):
        writer.writerow({'star_number': i+1, 'x': star['x'], 'y': star['y'], 'brightness': star['brightness'], 'radius': star['radius']})

"""
Prints the number of stars that were detected in stars object.
"""
print("Number of stars: {}".format(len(stars)))
