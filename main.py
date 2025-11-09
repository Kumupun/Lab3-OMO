import numpy as np
import termcolor as tc
import pwr_iter
import jacobi
import mod_newt

def print_menu():
    print(tc.colored("Menu:", "yellow"))
    print("1. Find smallest eigenvalue using Power Iteration method")
    print("2. Find eigenvalues using Jacobi method")
    print("3. Find solution using modified Newton method")
    print(tc.colored("4. Exit", "red"))

def main():
    print_menu()
    c= input("Choose an option (1-3): ")
    if c == '1':
        print("Power Iteration Method Selected")
        print("Enter initial guess :")
        x0 = np.array(list(map(float, input().split())))
        epsilon = float(input("Enter epsilon: "))
        max_iter = int(input("Enter maximum number of iterations: "))
        result = pwr_iter.pwr_iter(x0, epsilon, max_iter)
        if result is not None:
            print(tc.colored(f"MIN Eigenvalue = {result}", "green"))
        else:
            print(tc.colored("No eigenvalue found/converged.", "red"))
        return 0
    
    elif c == '2':
        print("Quadratic Method Selected.")
        print("Enter initial guess :")
        x0 = np.array(list(map(float, input().split())))
        result = quad.quad(x0)
        if result is not None:
            print(f"x = {result}")
        else:
            print("No root found.")
        return 0
    
    elif c == '3':
        print("Seidel's Method Selected.")
        print("Enter initial guess :")
        x0 = np.array(list(map(float, input().split())))
        epsilon = float(input("Enter epsilon: "))
        max_iter = int(input("Enter maximum number of iterations: "))
        result = seidel.seidel(x0, epsilon, max_iter)
        if result is not None:
            for i, val in enumerate(result):
                print(f"x{i} = {val}")
        else:
            print("No root found.")
        return 0
    
    elif c == '4':
        print("Exiting the program.")
        return 0
    return 0
main()