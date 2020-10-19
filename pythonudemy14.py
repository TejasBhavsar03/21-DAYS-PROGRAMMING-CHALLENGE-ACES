# Function Exercise:
# Calculate Factorial
def fact_fun(n):
    result = 1
    for n in range(2, n + 1):
        result = result * n
    return result


for i in range(1, 10):
    print(i, fact_fun(i))

# Calculate Factorial: Recursive
    print('x' * 20)


    def recursivefun(n):
        if n <= 1:
            return 1
        else:
            a = n * recursivefun(n - 1)
            return a


    for i in range(1, 10):
        print(i, recursivefun(i))


 #   Exercise Fabanucci Sequence

    def fib(n):

        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)


    for i in range(10):
        print(i, fib(i))