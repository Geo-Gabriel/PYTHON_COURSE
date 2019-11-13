

n = int(input('digite n: '))

p = i = 0

while n != 0:
    if n % 2 == 0:
        p = p + 1
    else:
        i = i + 1
    
print(p)
print(i)