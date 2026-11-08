import numpy as np

def gaussian_elimination(A, b):
    A = np.array(A, dtype=float)  
    b = np.array(b, dtype=float)
    n = len(A)
    x = np.zeros(n)

    for rc in range(n - 1):
        r = rc + np.argmax(np.abs(A[rc:, rc]))
        if r != rc:
            A[[rc, r], :] = A[[r, rc], :]
            b[[rc, r]] = b[[r, rc]]

        for i in range(rc + 1, n):
            u = A[i, rc] / A[rc, rc]
            A[i, :] = A[i, :] - u * A[rc, :]
            b[i] = b[i] - u * b[rc]

    for rc in range(n - 1, -1, -1):
        s = np.dot(A[rc, rc+1:], x[rc+1:])
        x[rc] = (b[rc] - s) / A[rc, rc]

    return x