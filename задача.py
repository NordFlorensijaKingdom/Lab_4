import random
numbers = [random.randint(1, 1000) for i in range(500)]

maxsum = 0
num1, num2 = 0, 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        cursum = numbers[i] + numbers[j]
        if cursum > maxsum:
            maxsum = cursum
            num1, num2 = numbers[i], numbers[j]

print(f"Два числа с максимальной суммой: {num1} и {num2}")
print(f"Максимальная сумма: {maxsum}")
