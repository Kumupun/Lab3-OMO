import numpy as np
import termcolor as tc

def jacobi(max_iter):
    A = np.array([
     [4, 0, 0, 1],
     [0, 3, 1, 2],
     [0, 1, 2, 0],
     [1, 2, 0, 3]
     ], dtype=float)
    B= A.copy()
    print(tc.colored(f"Initial Matrix B = \n{B}", "cyan"))
    
    for i in range(max_iter):
       bij = 0
       p,q = 0,0
       for n in range(len(B)):
           for m in range(n+1, len(B)):
               if  bij < abs(B[n][m]):
                   bij = abs(B[n][m])
                   p,q = n,m
       if bij > 0:
            theta = 0.5 * np.arctan2(2 * B[p][q], B[p][p] - B[q][q])
            print(f"Iteration {i+1}\nAngle theta = {np.degrees(theta)}")
            c = np.cos(theta)
            s = np.sin(theta)
            J = np.eye(len(B))
            J[p][p] = c
            J[q][q] = c
            J[p][q] = -s
            J[q][p] = s
            print(f"Jacobi Matrix J = \n{J}")
            B = J.T @ B @ J
            print(f"New matrix B = \n{B}")
    return np.diag(B)