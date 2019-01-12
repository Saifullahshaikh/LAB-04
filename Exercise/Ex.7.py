print('saifullah- 1bB-092-CS  A')
print('Lab-04, P.Ex.6')
A = [[1,0],
     [2,6]]
B = [[5,7],
     [8,4]]
C = [[0,0],
     [0,0,]]
for a in range(len(A)):
    for b in range(len(B)):
        for c in  range(len(B)):
            C[a][b] += A[a][c] * B[b][c]
for r in C:
    print(r)
