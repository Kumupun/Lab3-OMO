import numpy as np
import termcolor as tc

def mod_newton(x0, epsilon, max_iter):
    x = x0
    for i in range(max_iter):
        J = np.array([[2*x[0], 2*x[1]], [2*x[1], 2*x[0]]])
        f = np.array([x[0]**2 + x[1]**2 - 1, x[0]**2 - x[1]])
        delta = np.linalg.solve(J, -f)
        x += delta
        if np.linalg.norm(delta) < epsilon:
            print(tc.colored(f"Converged after {i} iterations.", "green"))
            return x
    print(tc.colored("Did not converge.", "red"))
    return None