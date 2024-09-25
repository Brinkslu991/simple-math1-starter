#Lucas Brinks
#9/25/24
#simple math

#Simple Math
num1 = int(input('Enter a #: '))
num2 = int(input('Enter a #: '))

sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2

print(f'{num1} plus {num2} = {sum}')
print(f'{num1} minus {num2} = {sub}')
print(f'{num1} times {num2} = {mult}')
print(f'{num1} divided by {num2} = {div}')
print(f'{num1} % {num2} = {mod}')

#Area Calulation
length = float(input('Enter the length: '))
width = float(input('Enter the width: '))

area = length * width

print(f'The width of your room is {width}, a length of {length}, and an area of your rectangular room is {area}')

#Formatting Numeric Output

# Part 1
name = input('Enter your name: ')
age = int(input('Enter your age: '))
color = input('Enter your favorite color: ')

text = 'My name is {0}, I am {1} years old, and {2} is my favorite color.'.format(name, age, color)

print(text)

# Part 2
STATE_SALES_TAX = 1.06

item_price = float(input('Enter item price: '))

total = item_price*STATE_SALES_TAX

print(f'your item was ${item_price:.2f} and your total is ${total:.2f}')

# Part 3

friends_name = 'Joshua'
friends_school = 'Alba'

friend = 'My friends name is {0} and they attend {1}.'.format(friends_name, friends_school)

print(friend)