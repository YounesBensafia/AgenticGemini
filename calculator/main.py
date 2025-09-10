import sys
from pkg.calculator import Calculator
from pkg.render import render


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        raise ValueError("Not enough arguments provided. Please provide an expression to evaluate. you need to use it like this: python main.py \"2 + 2 * 3\"")
    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")
    expression = " ".join(sys.argv[1:])
if __name__ == "__main__":
    main()