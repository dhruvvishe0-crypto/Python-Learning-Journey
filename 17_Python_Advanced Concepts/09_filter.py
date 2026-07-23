# filter is also called as high order function in python
# filter returns an iterables that contains elements from the iterable for which the function returns true

# for example :

numbers = [56,3,56,98,277,8,7,2,78,90,1,5,788]

def number_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False

print(list(filter(number_greater_than_9,numbers)))  # it returns filter object that why we have used list typecasting
