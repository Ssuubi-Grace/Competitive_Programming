n = int(input()) 
total = 0
max_capacity = 0

for _ in range(n):
    ai, bi = map(int, input().split())
    total -= ai
    total += bi
    max_capacity = max(max_capacity, total)

print(max_capacity)
