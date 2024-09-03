# Based on asking details from the user.

name = input('Enter your name:').split()
age = int(input('Enter your age:'))
location = input('Enter your location:')

if age < 0:
    print('Please enter a valid age.')
elif age < 18:
    print('You are a teenager.')
elif age >= 18 and age < 60:
    print('You are an adult.')
else: 
    print('You are an elder.')

print(f'Hello {name[0]} {name[1]}. You are {age} years old and live in {location}.')