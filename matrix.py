rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: ")) 
matrix=[]
for i in range(rows):
    row=[]
    for j in range(columns):
        row.append(int(input(f"Enter the element at position ({i},{j}): ")))
    matrix.append(row)
print(matrix)    