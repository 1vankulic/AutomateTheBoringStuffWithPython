userName = input()

print("It is good to meet you" + userName)

# do while in Python

while True:
    print("Who are you ?")
    name = input()

    if name != 'Joe':
        continue # continue jumps back to the start of the program
    
    print("Hello, Joe. What is the password? (It's a fish)")
    
    password = input()
    if password == 'swordfish':
        break # breaks out of the loop == continuing to next block of code
print("Access granted.") 

#  In fact, you can use continue and break statements only inside while and for loops
# If you try to use these statements elsewhere, Python will give you an error.