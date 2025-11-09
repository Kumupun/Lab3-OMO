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
        print("Jacobi Method Selected.")
        max_iter = int(input("Enter  number of iterations: "))
        result = jacobi.jacobi(max_iter)
        if result is not None:
            for i in range(len(result)):
                print(tc.colored(f"Eigenvalue {i+1} = {result[i]}", "green"))
        else:
            print(tc.colored("No eigenvector found.", "red"))
        return 0
    
    elif c == '3':
        print("Modified Newton Method Selected.")
        print("Enter initial guess :")
        x0 = np.array(list(map(float, input().split())))
        epsilon = float(input("Enter epsilon: "))
        max_iter = int(input("Enter maximum number of iterations: "))
        result = mod_newt.mod_newton(x0, epsilon, max_iter)
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