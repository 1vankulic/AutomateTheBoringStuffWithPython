## Local variables cannot be used in the global scope
# def spam():
#     eggs = 31457
# spam()
# print(eggs)


## Local scopes cannot use variables in other local scopes
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()


## Global variables can be read from a local scope
# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)


## Local and global variables with the same name
def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)