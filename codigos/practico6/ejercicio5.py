import numpy as np

def jacobi(A,b,err,mit):
    M = np.diag(np.diag(A))
    N = M - A
    Minv = np.diag(1/np.diag(M))
    x0 = np.zeros(b.shape)

    for k in range(mit):
        x1 = Minv @ ( N @ x0 + b)

        if np.linalg.norm(x1-x0, ord=np.inf) < err:
            break
        else:
            x0 = x1.copy()

    return [x1,k]
            

