import numpy as np

def get_matrix():
    while True:
        try:
            rows=int(input("Enter rows: "))
            columns=rows+1
            print(f"You will have {rows} rows and {columns} columns (including the solution column).")
            break
        except ValueError:
            print("That was not a number. Try again.")

    matrix=[]
    print("\nEnter the matrix values:")

    for i in range(rows):
        row=[]
        for j in range(columns):
            while True:
                try:
                    val=float(input(f"A[{i}][{j}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Invalid. Enter a number.")
        matrix.append(row)

    return np.array(matrix,dtype=float),rows,columns


def print_matrix(A):
    print(np.around(A,decimals=4))


def gauss_jordan(A,rows):
    A=A.copy()
    for i in range(rows):
        if A[i][i]==0:
            for k in range(i+1,rows):
                if A[k][i]!=0:
                    A[[i,k]]=A[[k,i]]
                    break

        A[i]=A[i]/A[i][i]

        for j in range(rows):
            if i!=j:
                A[j]=A[j]-(A[i]*A[j][i])

    return A


def print_solution(A,rows):
    for i in range(rows):
        print(f"x{i+1}={A[i][-1]:.4f}")


A,rows,columns=get_matrix()
print("\nOriginal matrix:")
print_matrix(A)

A2=gauss_jordan(A,rows)
print("\nReduced matrix:")
print_matrix(A2)

print("\nSolution:")
print_solution(A2,rows)
