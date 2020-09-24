### Problem 39 - Integer Right Triangles
###------------------------------------------------------------------------------------------------------------------------------------
### If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
### {20,48,52}, {24,45,51}, {30,40,50}
### For which value of p ≤ 1000, is the number of solutions maximised?

### Solution

import numpy as np
import math

py_triples = {}

for i in range(1, 1001):
    for j in range(i, 1001):
        k = np.sqrt(i ** 2 + j ** 2)
        if (k - math.floor(k)) == 0:
            p = i + j + k
            if p > 1000:
                continue
            if str(p) in py_triples:
                py_triples[str(p)] += 1
            else:
                py_triples[str(p)] = 1

max_solns = max(py_triples, key=py_triples.get)
print("The maximum number of solutions occur when p = " + str(max_solns))
