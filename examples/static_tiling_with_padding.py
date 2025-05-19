import numpy as np
import matplotlib.pyplot as plt

from ndtiler import tile_nd
from ndtiler import get_overflow

tile_size = (32, 32)

# Does NOT evenly divide the image, thus we need to pad the image
overlap = (10, 10)

image = np.zeros((256, 256))
print("Image shape before padding:", image.shape)

# Get the overflow needed to make the image evenly divisible by the tile size
overflow = get_overflow(image.shape, tile_size, overlap)
image = np.pad(image, ((0, overflow[0]), (0, overflow[1])), mode = "constant")
print("Image shape after padding:", image.shape)

for ((y0, y1), (x0, x1)) in tile_nd(image.shape, tile_size, overlap):
    image[y0:y1, x0:x1] += 1

plt.imshow(image)
plt.show()
