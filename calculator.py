import sys
import math

def add(numbers):
    return sum(numbers)

def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def exponentiate(base, exp):
    return math.pow(base, exp)

def root(base, nth):
    return base ** (1/nth)

def log(base, value):
    return math.log(value, base)

def calculate(args):
    operation = args[1]
    numbers = list(map(float, args[2:]))

    if operation == 'add':
        return f"Sum: {add(numbers)}"
    elif operation == 'multiply':
        return f"Product: {multiply(numbers)}"
    elif operation == 'exponentiate':
        return f"{numbers[0]}^{numbers[1]}: {exponentiate(numbers[0], numbers[1])}"
    elif operation == 'root':
        return f"{numbers[1]}-root of {numbers[0]}: {root(numbers[0], numbers[1])}"
    elif operation == 'log':
        return f"Log base {numbers[1]} of {numbers[0]}: {log(numbers[1], numbers[0])}"
    else:
        return "Invalid operation"

def main():
    if len(sys.argv) < 3:
        print("Usage: python calculator.py <operation> <numbers...>")
        return

    result = calculate(sys.argv)
    print(result)

if __name__ == "__main__":
    main()
