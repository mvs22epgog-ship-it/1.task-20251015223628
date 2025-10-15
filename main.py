def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    fact1 = factorial(num1)
    fact2 = factorial(num2)
    
    sum_of_factorials = fact1 + fact2
    
    print(f"Factorial of {num1} is {fact1}")
    print(f"Factorial of {num2} is {fact2}")
    print(f"Sum of factorials is {sum_of_factorials}")

if __name__ == "__main__":
    main()
