import numpy as np
x = np.ones((3, 3))
print(x)
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)

