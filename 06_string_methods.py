name = 'Asadullah Al Galib'
print('No. of chars: ', len(name))
print(name.upper())
print(name.lower())

# find() func returns the idx of the first found char in string

print(name.find('a'))
print(name.find('Galib')) # returns the idx of G
print(name.replace('Galib', 'Good Galib'))

bool_result = 'Galib' in name
print(bool_result)