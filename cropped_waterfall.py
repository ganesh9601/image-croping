import cv2
import numpy as np

# Load the image using OpenCV
image = cv2.imread('waterfall.jpg')
print(image.shape)
# Define the coordinates or parameters for different shapes
# Rectangle
rect_x, rect_y, rect_w, rect_h = 100, 100, 200, 150

# Square
square_side = 150

# Triangle
triangle_points = np.array([(300, 100), (450, 100), (375, 250)], np.int32)
# print(triangle_points)
# Hexagon
hexagon_points = np.array([
    (200, 400), (100, 300), (150, 200),
    (250, 200), (300, 300), (250, 400)
], np.int32)
# print(hexagon_points)
# Create masks for different shapes
rect_mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.rectangle(rect_mask, (rect_x, rect_y), (rect_x + rect_w, rect_y + rect_h), 255, -1)

square_mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.rectangle(square_mask, (rect_x, rect_y), (rect_x + square_side, rect_y + square_side), 255, -1)

triangle_mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.fillPoly(triangle_mask, [triangle_points], 255)

hexagon_mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.fillPoly(hexagon_mask, [hexagon_points], 255)

# Apply masks to the image
cropped_rect = cv2.bitwise_and(image, image, mask=rect_mask)
cropped_square = cv2.bitwise_and(image, image, mask=square_mask)
cropped_triangle = cv2.bitwise_and(image, image, mask=triangle_mask)
cropped_hexagon = cv2.bitwise_and(image, image, mask=hexagon_mask)

# Save the cropped images
cv2.imwrite('cropped_rectangle.jpg', cropped_rect)
cv2.imwrite('cropped_square.jpg', cropped_square)
cv2.imwrite('cropped_triangle.jpg', cropped_triangle)
cv2.imwrite('cropped_hexagon.jpg', cropped_hexagon)