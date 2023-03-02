N, M = map(int, input().split())

A, B = [], []
result = []

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    temp = []
    for z in range(M):
        temp.append(A[i][z] + B[i][z])
    result.append(temp)

for i in result:
    for z in i:
        print(z, end=' ')
    print()
exit()