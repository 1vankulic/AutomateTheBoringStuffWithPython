# Python adds return None to the end of any function definition with no return statement. 
# This is similar to how a while or for loop implicitly ends with a continue statement. 
# Also, if you use a return statement without a value 
# (that is, just the return keyword by itself), then None is returned.

print('Hello', end=' ')
print('World') # prints Hello World

print('Hello') # prints Hello                
print('World') # World

print('cats', 'dogs', 'mice')
# cats dogs mice

print('cats', 'dogs', 'mice', sep=', ')
# cats, dogs, mice
