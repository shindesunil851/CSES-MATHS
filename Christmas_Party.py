m = 10**9 + 7
a, b = 0, 1
for i in range(int(input())):
    a, b = b, (a + b) * i % m
print(b)