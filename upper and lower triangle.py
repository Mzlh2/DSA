rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
matrix=[]
for i in range(rows):
    rowarray=[]
    for j in range(columns):
        rowarray.append(int(input("Enter the value: ")))
    matrix.append(rowarray)
print(matrix)
for r in range(rows): 
    for c in range(columns):
        print(matrix[r][c], end=" ")
    print()
# for r in range(rows-1):
#     for c in range(r+1,columns):
#         print(matrix[r][c], end=" ")
#     print()
# for r in range(1,rows):
#     for c in range(r):
#         print(matrix[r][c], end=" ")
#     print() 
print("Transpose of matrix:")  
transpose=[[0 for c in range(columns)] for r in range(rows)] 
for r in range(rows):
    for c in range(columns):
        transpose[r][c]=matrix[c][r]
print(transpose)


