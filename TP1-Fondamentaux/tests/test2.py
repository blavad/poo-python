import numpy as np
from tp1.math import addition, np_addition


print("> ------------------------------")
print("> Test partie 1")
print("> ------------------------------")
print(f"> Test addition : {addition(8,9)==17}")
print(f"> Test np_addition : {np.array_equal(np_addition([8,9],[5,1]), np.array([13,10]))}")
print("> ------------------------------")