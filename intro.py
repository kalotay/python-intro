# declaring things

# numbers
1
2
3
0
-1
528123
3.14
0.5
10e10

# strings
'hello'
"now eith double quotes"
"double quotes
can span
many lines"
'\\ is the escape character'

# boolean
True
False

# None (aka null, nil)
None

# assigning values to variables
a_number = 9876
a_string = 'hi again'

# interacting with python
print(1)
print('more stuff')
# variables can be reffered to
print(a_number)
print(a_string)

# what is print, it is a function
# there are others for example len
a_length = len(a_string)
print(a_length)
# don't need to declare a new variable
print(len(a_string))

# defining functions
def print_length(lengthy):
    length = len(lengthy)
    print(length)

# functions return values (None by default)
def absolute_power(x, y):
    return pow(abs(x), abs(y))

a_power = absolute_power(-5, -2)
print(a_power)

# arithmetic is implemented
three_fifths = 1 + 2 - 3 * 4 / 5
# plus can be used to concatenate strings
whole = 'left' + 'right'

# functions are values
abs_value = abs
print(abs_value(-10))

# compound types
# lists
a_list = [1, 2, 3]
first = a_list[0]
second = a_list[1]
last = a_list[-1]
a_list[0] = 5
# tuples
a_tuple = (0, 'hi')
first = a_tuple[0]
# dictionaries
a_dict = {'python': 'dynamic', 'c#': 'static'}
python_compilation = a_dict['python']
a_dict['ruby'] = 'dynamic'

# control flow
# for loops for iterables like list
for number in a_list:
    print(a_number)
for key in a_dict:
    print(key)

# if statements
# truthy and falsy values
if s == 'fizz':
    print('divisble by 3')
elif s == 'buzz':
    print('divisible by 5')
else:
    print('other')

# while loop
countdown = 5
while countdown > 0:
    print(countdown)
    countdown += 1

# functions can have misc positional and keyword arguments

# classes
class SomeClass(object):
    # constructor
    def __init__(self, some_value):
        self.some_value = some_value

    def print_value(self, print_func=print):
        print_func(self.some_value)

a_obj = SomeClass(10)
a_obj.print_value()

# exceptions
# handling
try:
    stuff
except Exception as e:
    handle
finally:
    always
# raising

# pass for empty statements

# import statements for modules
