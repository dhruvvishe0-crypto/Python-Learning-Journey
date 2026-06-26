# Recursion

# Recursion is a technique where a function solves a problem by calling itself again and again until it reaches a stopping condition.


def factorial(n):
    if n == 1:
        return 1
    else : 
        return n* factorial(n-1)
    
print(factorial(6))


def numbers_from_1_n(n):
    if n <=0:
        return
    else :
        numbers_from_1_n(n-1)
        print(n)


numbers_from_1_n(100)