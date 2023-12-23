
import numpy as np

# calculate determinant
def determinant(x):
    # deleting last coloumn of augmented matrix and makes it a square matrix
    matrix = np.delete(x, -1, axis=1) 
    deter = np.linalg.det(matrix) # calculate determinant
    return deter

# Receiving info from inputs
while True:
    rows = int(input("enter number of rows: "))
    coloumns = int(input("enter number of columns: "))
    if coloumns == rows:
        break
    else:
        print("numbers of rows and columns must be equal!") 
        # matrix must be square

# defining augmented matrix 
aug_matrix = []

# Receiving elements of matrix (Left hand side)
for i in range(rows):
    counter_01 = 0
    counter_02 = 0
    counter_03 = 0
    counter_01 += 1
    print("(row ", counter_01, ")")
    ar_02 = []
    for j in range(coloumns):
        counter_02 += 1
        print("column ", counter_02, ": ")
        elements = float(input())
        ar_02.append(elements)

    # Receiving answers of equasions (Right hand side)
    counter_03 += 1
    print("b", counter_03, ": ")
    b = float(input())
    ar_02.append(b)
    aug_matrix.append(ar_02)

# showing what is going to be solved
print("solving matrix: ")
print(aug_matrix)

# defining i and j for elementary row operations and lenght of the matrix and a zero matrix
X = np.zeros(length)
length = len(aug_matrix)
i = 0
j = i - 1

# using elementary row operations to making an upper triangular matrix 
while True:
    if determinant(aug_matrix) == 0:
        print("the determinant is 0, I can't solve this! ")
        break
    else:
        for i in range(i, length - 1):
            for j in range(i + 1, length):
                scale = aug_matrix[j][i] / aug_matrix[i][i]
                aug_matrix[j] = np.array(aug_matrix[j]) - scale * np.array(aug_matrix[i])
                print(aug_matrix)

        # using backward-method to solve Xs
        for i in range(length - 1, -1, -1):
            if aug_matrix[i][i] != 0:
                X[i] = aug_matrix[i][-1] / aug_matrix[i][i]
                for j in range(i - 1, -1, -1):
                    aug_matrix[j][-1] -= aug_matrix[j][i] * X[i]
            else:
                print("rank < lenght, Infinite solution for X")

        # Outputting the final results
        print("Solution for X:")
        for i, sol in enumerate(X):
            print("X{} = {:.2f}".format(i+1, round(sol, 2)))

    break