import numpy
import numpy as np
from PIL import Image

# Create 3d numpy array of zeroes, then replace zeroes (black pixels) with yellow pixels
data = numpy.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# Make a red patch
data[0:3, 0:2] = [255, 0, 0]
data[3:4, 1:4] = [20, 200, 0]

img = Image.fromarray(data, "RGB")
img.save("canvas.png")
