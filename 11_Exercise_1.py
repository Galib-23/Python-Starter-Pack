# Create a weight converter

weight = int(input('Enter weight: ')) # inputs generally string
unit = input('(L)bs or (k)g: ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} Kg")
else:
    converted = weight / 0.45
    print(f'You are {round(converted)} pounds')