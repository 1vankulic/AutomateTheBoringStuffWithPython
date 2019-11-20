# import random 

# for i in range(5):
#     print(random.randint(1, 10))

# or

# from random import *

# for i in range(5):
#     print(randint(1, 10))


from random import randint

for i in range(10000):
    b = randint(0, 10000)
    if b == 3000:
        print("Number 3000 came up")
    
# NEVER NAME YOUR FILES AS IMPORT MODULES
# eg. naming your file random then trying to import random