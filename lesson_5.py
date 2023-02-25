from random import randint as generate_number, choice
from calculator import addition, subtraction
from person import Person
from termcolor import colored, cprint
import emoji
from decouple import config

print(generate_number(1, 10))
print(addition(6, 2))
teacher = Person('Jim', 34)
print(teacher)
cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
num = config('COMMENTED', default='0', cast=int)
print(num * 3)

