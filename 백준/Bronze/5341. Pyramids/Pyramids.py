while True:
    a = int(input())
    if a == 0:
        break
    r = a
    while a != 1:
        r = r + (a - 1)
        a = a - 1
    print(r)