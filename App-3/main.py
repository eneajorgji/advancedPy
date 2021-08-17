from canvas import Canvas
from shapes import Rectangle, Square

# Get tge canvas width and height from the use
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

while True:
    shape_type = input("What would you like to draw? Enter quit to quit. ")

    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the rectangle
        r1 = Rectangle(rec_x, rec_y, rec_height, rec_width, (red, green, blue))
        r1.draw(canvas)

    #  Ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter the side length  of the square: "))
        red = int(input("How much red? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the square
        s1 = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        s1.draw(canvas)

    canvas.make("canvas.png")

    # Break the loop if the user enter quit
    if shape_type == "quit":
        break
