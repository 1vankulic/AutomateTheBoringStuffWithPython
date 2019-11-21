# def spam(divide_By):
#     try:
#         return 42 / divide_By
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')


def spam(divide_By):
    return 42 / divide_By

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

# The reason print(spam(1)) is never executed is 
# because once the execution jumps to the code in the except clause, 
# it does not return to the try clause. Instead, it just continues moving down as normal.







    