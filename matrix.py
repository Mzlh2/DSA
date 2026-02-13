rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: ")) 
matrix=[]
'''for i in range(rows):
     row=[]
     for j in range(columns):
         row.append(int(input(f"Enter the element at position ({i},{j}): ")))
     matrix.append(row)
print(matrix)'''   
for _ in range(rows):
    row=[]
    for _ in range(columns):
        value=int(input("Enter the value: "))
        row.append(value)
    matrix.append(row)  
print(matrix) 
#traversal of a matrix
for i in range(rows): 
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()