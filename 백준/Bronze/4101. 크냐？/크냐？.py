l = []
while True:
    
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    l.append([a, b])

for i in l:
    if i[0] <= i[1]:
        print('No')
    else:
        print('Yes')