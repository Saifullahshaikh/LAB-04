print('saifullah- 1bB-092-CS  A')
print('Lab-04, P.Ex.6')
A = [[5,6],
     [4,6]]
B = [[9,0],
     [7,3]]
C = [[0,0],
     [0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        C[i][j] = [A[i][j] + B[i][j]]
for r in C:
    print('C =', r)
     
