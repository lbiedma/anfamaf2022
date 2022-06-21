import numpy as np

def soltrsup(A, b):
    n = len(b)
    x = b.copy()
    # if np.prod(np.diag(A)) == 0:
    #     print("La matriz no es inversible")
    #     return None
    for i in reversed(range(n)):
        if A[i, i] == 0:
            print("La matriz no es inversible")
            return None
        for j in reversed(range(i+1, n)):
            x[i] = x[i] - A[i, j] * x[j]
        x[i] = x[i] / A[i, i]
    
    return x

def test_soltrsup():
    U = np.array([
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1],
    ], dtype="float"
    )
    b = np.array([3, 2, 1], dtype="float")
    print(soltrsup(U, b)) # Nos deberia dar [1, 1, 1]

# test_soltrsup()
