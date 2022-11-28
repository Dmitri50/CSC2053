import math
print("hello world!")
# This is a comment
'This is also a comment'
'''
This is how you would comment a function
or if you have many line of code to comment
'''

# line 1
# line 2
# line 3
# line 4

int_example = 5
float_example = 5.5
x = 5
x = "this is a string"

result = 5.5 // 4
print(result)

result = 5.5 % 4
print(result)

squared = 5 ** 2
print(squared)
squared = math.pow(5,2)
print(squared)

if squared == 25:
    print("correct")
else:
    print("something went wrong")

x = 10
y = 100

if x >= 10 or y < 90:
    print("one statement is true")

grade = 90
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
else:
    letter = "D"

if x > 10:
    print("error")

first_name = "Dmitri"
last_name = "Gaspard"
full_name = first_name + last_name
repeat = first_name * 5

first_two = first_name[0:2]
middle = first_name[2:4]

if 'Dmit' in first_name:
    print("d is the first letter")

def hello(name):
    print("Hello", name)

def hello_default_arg(name = "To whome it may concern"):
    print("hello ", name)

hello_default_arg("Joe")
hello_default_arg()

def return_two():
    return 1,5

x,y = return_two()
print(x,y)