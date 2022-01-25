
# Задание 1
print("Задание 1")
def geom(a, end):
    i = 1
    while a < end:
        res = i * a
        yield res
        i += 1

for i in geom(2, 20):
    print(i)

# Задание 2
print("\nЗадание 2")
def my_range(*args):
    start = stop = step = None
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    else:
        start = args[0]
        stop = args[1]
        step = args[2]

    while start < stop:
        yield start
        start += step

for i in my_range(10):
    print(i)

# Задание 3
print("\nЗадание 3")
def price_seq(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

for item in price_seq(10):
    print(item)

# Задание 4
print("\nЗадание 4")
x = []
y = (x.append(item ** 3) for item in range(10))
print(y)
print(x)

while True:
    try:
        next(y)
    except:
        break

print(x)