def son_reciprocos(x, y):
    if abs(x * y - 1) < 1e-7:
        return True
    else:
        return False

import random
for _ in range(100):
    x = 1 + random.random()
    y = 1 / x
    if not son_reciprocos(x, y):
        print(x)
        
