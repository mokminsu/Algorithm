a, b = [], []
for i in range(1, 31):
    a.append(i)
for i in range(1, 29):
    b.append(int(input()))
    
c = list(set(a) - set(b))
c.sort()
for i in c:
    print(i)

