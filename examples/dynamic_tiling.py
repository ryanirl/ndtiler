import numpy as np
import matplotlib.pyplot as plt

from ndtiler import dynamic_tile_nd

tile_size = (32, 32)

# Dynamic tiling does not require the tile size to evenly divide the image
overlap = (10, 10)

image = np.zeros((256, 256))

for ((y0, y1), (x0, x1)) in dynamic_tile_nd(image.shape, tile_size, overlap):
    image[y0:y1, x0:x1] += 1

plt.imshow(image)
plt.show()
