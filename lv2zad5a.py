import numpy as np 
import matplotlib.pyplot as plt 

def colored (square_size, square_height, square_width):
    red_square = np.ones((square_size, square_size, 3), dtype=np.uint8) * [255, 0, 0]
    blue_square = np.ones((square_size, square_size, 3), dtype=np.uint8) * [0, 0, 255]
    rows = []
    for i in range(square_height):
        row = []
        for j in range(square_width):
            if (i+j) % 2 == 0:
                row.append(red_square)
            else:
                row.append(blue_square)
        rows.append(np.hstack(row))
    img = np.vstack(rows)
    return img.astype('uint8')

img = colored (50, 4, 5)
plt.imshow(img)
plt.show()