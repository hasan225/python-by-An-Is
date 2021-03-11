def num (*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

print(num (10,20))