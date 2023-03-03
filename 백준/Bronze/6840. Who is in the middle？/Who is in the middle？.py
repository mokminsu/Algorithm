a = int(input())
b = int(input())
c = int(input())

l = [a, b, c]
l.remove(min(l))
l.remove(max(l))
print(l[0])