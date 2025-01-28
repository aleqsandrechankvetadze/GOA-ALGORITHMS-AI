def func1(a,b,c):
    count = 0
    if a > b:
        while b <= a:
            if b % c == 0:
                count += 1
            b += 1
    else:
        while a <= b:
            if b % c == 0:
                count += 1
            b += 1

    return count

print(func1(60, 50, 10))