from canvas import Canvas
from shapes import Rectangle, Square

canvas = Canvas(20, 30, (255, 255, 255))
r1 = Rectangle(1, 6, 7, 10, (100, 200, 125))
r1.draw(canvas)

s1 = Square(1, 3, 3, (0, 100, 222))
s1.draw(canvas)
canvas.make("canvas.png")
