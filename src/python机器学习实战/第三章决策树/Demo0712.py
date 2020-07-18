# AUTHOR lijixin

import numpy as np


print(np.random.seed(0))
p = np.array([0.95, 0.04, 0.01])
print(p)
index = np.random.choice([np.random.randint(800, 900), np.random.randint(400, 600), np.random.randint(100, 400)],p=p.ravel())
print(int(index))