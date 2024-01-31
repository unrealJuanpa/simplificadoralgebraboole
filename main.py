import numpy as np
import os
from utils import *

# condiciones: 
# 1. todos los ejemplos de la misma longitud
os.system('cls')

X = [
    "0001",
    "0010",
    "0011",
    "0100",
    "0101",
    "1001",
    "1010",
    "1101",
    "1110"
]

# minuscula = 0, mayuscula = 1
for i in range(len(X)):
    X[i] = binstr2keystr(X[i])


res = []

while len(X) >= 2:
    a = X.pop(0)
    idx = idxsimilarity(base=a, data=X, cid=-1)
    b = X.pop(idx)
    res = res + simplify(a, b)
    print(a)
    print(b)
    print()

# se agrega el residuo
res = res + X

print('residuo:')
print(X)

print()

print(res)