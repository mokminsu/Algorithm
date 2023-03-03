a = [i for i in range(1, 31)]
for i in range(1, 29):
    a.remove(int(input()))
print(min(a))
print(max(a))