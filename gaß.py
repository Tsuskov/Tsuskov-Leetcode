import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    # Forward elimination
    for i in range(n):
        # Pivoting
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if A[max_row, i] == 0:
            print("No unique solution")
            return None
        # Swap rows
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        # Eliminate
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x

n = int(input("Enter the number of variables: "))
A_list = []
b_list = []
for i in range(n):
    coeffs = input(f"Enter coefficients of equation {i+1}, separated by spaces: ")
    A_list.append([float(num) for num in coeffs.strip().split()])
    constant = float(input(f"Enter constant term of equation {i+1}: "))
    b_list.append(constant)
A = np.array(A_list, dtype=float)
b = np.array(b_list, dtype=float)
solution = gauss_elimination(A, b)
if solution is not None:
    print("Solution x:", solution)


