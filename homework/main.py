# code for matrix input from user

R = int(input("Enter the number of rows:"))#sıra
C = int(input("Enter the number of columns:"))#sütun

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):  # A 'for loop' for row entries
    a = []
    for j in range(C):  # A 'for loop' for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
