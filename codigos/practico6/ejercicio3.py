import numpy as np
from scipy import linalg

from ejercicio1 import soltrsup #, soltrinf

def sollu(A, b):
    P, L, U = linalg.lu(A)

    b_tilde = P.T @ b
    y = np.linalg.solve(L, b_tilde) # esto deberia ser soltrinf(L, b_tilde)
    x = soltrsup(U, y)

    return x

def test_sollu():
    A = np.array([
        [3, 1, 1],
        [2, 6, 1],
        [1, 1, 4],
    ], dtype="float"
    )
    b = np.array([5, 9, 6], dtype="float")
    print(sollu(A, b)) # Nos deberia dar [1, 1, 1]

test_sollu()
