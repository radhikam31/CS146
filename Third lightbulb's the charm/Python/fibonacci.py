def fibonacci(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

if __name__ == "__main__":
    n = 9 
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")


#Output: The 9th Fibonacci number is: 34