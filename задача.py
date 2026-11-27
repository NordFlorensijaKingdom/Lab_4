import random
numbers = [random.randint(1, 1000) for i in range(500)]

max1 = max2 = numbers[0]

for x in numbers:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x

print(max1, max2, max1 + max2)
print(numbers)
