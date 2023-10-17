mat1=[[20,2,7],[3,5,9],[1,6,5]]
mat2=[[1,4,3],[2,2,5],[3,2,2]]
mat3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            mat3[i][j] += mat1[i][k] * mat2[k][j]
print("The new matrix formed after multiplication is : ")
for r in mat3:
    print(r)
