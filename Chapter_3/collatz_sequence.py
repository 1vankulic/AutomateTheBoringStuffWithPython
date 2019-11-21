def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    if number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

try:
    user_input = int(input("Enter number: "))
    while user_input != 1:
        user_input = collatz(user_input)
except ValueError:
    print("Input must be an integer")




