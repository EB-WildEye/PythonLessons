# EMatrix

# Matrix is list inside of list
row1 = [1, 2, 3, 4]
row2 = ['Shay', 'Ron', 'Agam', 'Shilat']
row3 = [True, False, True, False]

matrix1 = [row1, row1, row1]
matrix = [[1, 2, 3, 4], ['Shay', 'Ron', 'Agam', 'Shilat'], [True, False, True, False]]
print(matrix)

for row in range(len(matrix)): # עוברת על כל רשימה פנימית  matrix[0], matrix[1]
    for col in range(len(matrix[0])): # עוברת על כל איבר ברשימה הפנימה matrix[row][col]
        print(matrix[row][col])

