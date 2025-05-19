import numpy as np

from ndtiler import tile_nd
from ndtiler import dynamic_tile_nd

# Create a sample 2D array
data = np.zeros((512, 512))

# Define tile size and overlap
tile_size = (128, 128)
overlap = (32, 32)

# Generate tile coordinates using static tiling
for ((y0, y1), (x0, x1)) in tile_nd(data.shape, tile_size, overlap):
    tile = data[y0:y1, x0:x1]  # Extract the tile

    #
    # Process the tile...
    #

    
# Generate tile coordinates using dynamic tiling
for ((y0, y1), (x0, x1)) in dynamic_tile_nd(data.shape, tile_size, overlap):
    tile = data[y0:y1, x0:x1]  # Extract the tile

    #
    # Process the tile...
    #

