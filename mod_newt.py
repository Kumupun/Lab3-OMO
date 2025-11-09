import numpy as np
import termcolor as tc

def mod_newt(x0, epsilon, max_iter):
    F = lambda x, y: np.array([
        np.sin(2*x - y) - 1.2*x - 0.4,
        0.8*x**2 + 1.5*y**2 - 1
    ], dtype=float)
    
    Ak = lambda x, y: np.array([
        [2*np.cos(2*x - y) - 1.2, -np.cos(2*x - y)],
        [1.6*x, 3*y]
    ], dtype=float)
    
    A0_ = np.linalg.inv(Ak(x0[0], x0[1]))
    print(f'Обернена матриця обчислена в початковій точці A0_ = \n{A0_}\n')
    
    xn = x0.copy().astype(float)
    for n in range(max_iter):
        Fxn = F(xn[0], xn[1])
        x_old = xn.copy()
        xn = x_old - A0_ @ Fxn

        print(f'Ітерація {n}: x = {xn}')

        if np.linalg.norm(xn - x_old, ord=2) < epsilon:
            print(tc.colored(f'Збіг після {n+1} ітерацій.', 'green'))
            return xn

    print(tc.colored('Перевищено максимальну кількість ітерацій. Розв’язок не знайдено.', 'red'))
    return None
