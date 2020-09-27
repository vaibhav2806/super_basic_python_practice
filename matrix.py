x = int(input("ENTER  THE NUMBER OF ROWS :"))
y = int(input("ENTER THE NUMBER OF COLUMNS :"))
matrix = []

print("ENTER THE ELEMENTS ROWISE :")

for i in range(x):                                 #TO TAKE INPUT FROM USER 
    a = []
    for j in range(y):
        a.append(int(input()))
    matrix.append(a)

for i in range (x):                                #TO PRINT THE MATRIX
    for j in range (y):
        print(matrix[i][j], end = " ")
    print( )
    