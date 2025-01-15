#factorial of 10

# using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(10)
print(result)

# Using for loop
result = 1
for i in range(1,11):
    result *= i
print(result)