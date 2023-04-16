import numpy as np 
import matplotlib.pyplot as plt 

def blackandwhite (square_size, square_height, square_width):
    black_square = np.zeros((square_size, square_size))
    white_square = np.ones((square_size, square_size)) * 255
    rows = []
    for i in range(square_height):
        row = []
        for j in range(square_width):
            if (i+j) % 2 == 0:
                row.append(black_square)
            else:
                row.append(white_square)
        rows.append(np.hstack(row))
    img = np.vstack(rows)
    return img.astype('uint8')

img = blackandwhite (50, 4, 5)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()