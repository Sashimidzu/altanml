import numpy as np
X = np.ones((10, 10))
X[1:-1,1:-1] = 0
print(X)
