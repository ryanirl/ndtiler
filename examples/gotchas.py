import numpy as np
import matplotlib.pyplot as plt

from ndtiler import dynamic_tile_nd

# An error will be raised if the tile size is too large. This should be checked
# beforehand using `get_overflow()` by the developer. 
tile_size = (512, 512)

overlap = (10, 10)

image = np.zeros((256, 256))

for ((y0, y1), (x0, x1)) in dynamic_tile_nd(image.shape, tile_size, overlap):
    image[y0:y1, x0:x1] += 1

plt.imshow(image)
plt.show()
