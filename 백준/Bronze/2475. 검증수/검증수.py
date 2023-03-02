numbers = list(map(lambda x: x * x, map(int, input().split())))

print(sum(numbers) % 10)