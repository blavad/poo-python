import numpy as np
from typing import List

list_ent=List[int]

def np_addition(a:list_ent,b:list_ent):
    a=np.array(a)
    b=np.array(b)
    return a+b