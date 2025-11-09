import numpy as np
import termcolor as tc

def pwr_iter(x0, epsilon, max_iter):
    A = np.array([
     [4, 0, 0, 1],
     [0, 3, 1, 2],
     [0, 1, 2, 0],
     [1, 2, 0, 3]
     ], dtype=float)

    a = np.linalg.inv(A.copy())
    val_old = 0.0
    x_old = x0 / np.linalg.norm(x0)
    for i in range(max_iter):
        x = a @ x_old / np.linalg.norm(a @ x_old)
        print(f"Iteration {i+1}\nInverse matrix eigenvector = {x}")
        val = (x.T @ a @ x) / (x.T @ x)
        minval = 1 / val
        print(f"MIN Eigenvalue = {minval}")
        if abs(val - val_old) < epsilon:
            print(tc.colored(f"Converged after {i+1} iterations.", "green"))
            return minval
        val_old = val
        x_old = x 
    print(tc.colored("Maximum iterations reached without convergence.", "red"))
    return None