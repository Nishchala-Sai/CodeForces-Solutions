rows=5
columns=5
matrix=[]
for i in range(rows):
    l=list(map(int, input().split()))
    matrix.append(l)
centre_x,centre_y=3,3
x,y=0,0
for i in range(1,6):
    for j in range(1,6):
        if matrix[i-1][j-1]==1:
            x,y=i,j
moves=0
moves+= abs(x-centre_x) #how much away on x-axis
moves+= abs(y-centre_y) #how much away on y-axis
print(moves)