x = 1
y = 2
fib = x + y
sum = y

while fib < 4000000:
    if fib % 2 == 0:
        sum += fib
    x = y
    y = fib
    fib = x + y

print(sum)