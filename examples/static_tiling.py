import numpy as np
import matplotlib.pyplot as plt

from ndtiler import tile_nd

# Define tiling parameters
tile_size = (32, 32)
overlap = (4, 4)

image = np.zeros((256, 256))

for ((y0, y1), (x0, x1)) in tile_nd(image.shape, tile_size, overlap):
    image[y0:y1, x0:x1] += 1

plt.imshow(image)
plt.show()
