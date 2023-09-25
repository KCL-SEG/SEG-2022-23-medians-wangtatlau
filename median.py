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
        
lengthOfNum = len(numbers)
sumOfNum = sum(numbers)
medianOfNum = sumOfNum/lengthOfNum

print(numbers)
