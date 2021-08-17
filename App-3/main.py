from PIL import Image
import numpy as np


class Canvas:
    """Object where all shapes are going to be drawn"""

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)


class Rectangle:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


canvas = Canvas(20, 30, (255, 255, 255))
r1 = Rectangle(1, 6, 7, 10, (100, 200, 125))
r1.draw(canvas)

s1 = Square(1, 3, 3, (0, 100, 222))
s1.draw(canvas)
canvas.make("canvas.png")
