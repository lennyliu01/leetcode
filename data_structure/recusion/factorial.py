# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!  
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
