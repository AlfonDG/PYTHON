n = int(input("Enter a number to calculate its Fibonacci sequence: "))

def fibonacci(n):

    print(f"Calculating fibonacci({n})")

    if n == 0:

        result = 0

    elif n == 1:

        result = 1

    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    print(f"fibonacci({n}) = {result}")

    return result

print(fibonacci(n))