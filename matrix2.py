rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
matrix=[]
for i in range(rows):
    rowarray=[]
    for j in range(columns):
        rowarray.append(int(input("Enter the value: ")))
    matrix.append(rowarray)
print(matrix)
# visiting all the elements in a data structure is called traversal
# 1.row-wise traversal      2.column-wise traversal
# row-wise traversal-pick one row and visit all the values in that row and then move to the next row
# column-wise traversal-pick one column and visit all the values in that column and then move to the next column 
# to visit any cell in a matrix, we write the matrix name, then row index then column index.
'''for rowindex in range(rows):
    for columnindex in range(columns):
        print(matrix[columnindex][rowindex], end=" ")
    print()'''
'''for rowindex in range(rows):
    print(matrix[rowindex][rowindex], end=" ")     #primary diagonal traversal
print()'''
# for k in range(rows):
#     print(matrix[k][columns-1-k], end=" ")     #secondary diagonal traversal  
# print()

# write a program to find the sum of all the elements in a row
'''for i in range(rows):
    sum = 0
    for j in range(columns):
        sum += matrix[i][j]
    print(f"Sum of row {i}: {sum}") '''

'''for i in range(columns):
    sum = 0
    for j in range(rows):
        sum += matrix[j][i]
    print(f"Sum of column {i}: {sum}")'''

'''sum=0
for i in range(rows):
    sum+=matrix[i][i]
print(f"Sum of primary diagonal: {sum}")'''

sum=0
for i in range(rows):
    sum+=matrix[i][columns-1-i]
print(f"Sum of secondary diagonal: {sum}")    