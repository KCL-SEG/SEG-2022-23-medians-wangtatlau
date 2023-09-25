"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
lengthOfNum = len(numbers)

if lengthOfNum % 2 == 0:
    medianNum = (numbers[int(lengthOfNum/2)] + numbers[int(lengthOfNum/2) - 1]) / 2
else:
    medianNum = numbers[int(lengthOfNum/2)]

print(medianNum)
