import random

FirstName = ['Crimson', 'Soul', 'Midnight', 'Twilight', 'Dark', 'Awkward', 'Red', 'Cerulean',  ]

# Add more names to this

SecondName = ['Runner', 'Flower', 'Blade', 'Moon']

# Add more names to this

FN = random.choice(FirstName)
SN = random.choice(SecondName)
GameName = FN + ' ' + SN

print("Your gammer's name is: " + GameName)
