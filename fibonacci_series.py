def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
num = int(input("Enter how many Fibonacci numbers to print: "))
print("Fibonacci series:", fibonacci(num))
