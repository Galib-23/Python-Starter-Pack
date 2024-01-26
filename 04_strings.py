#multi line strings----->
email = '''
Hello Mr, 
    How are you doing?
    I hope you are doing well.
Best wishes
'''
print(email)

#INDEX -------->
name = 'Asadullah Al Galib'

print('The char of 0th idx: ' + name[0])
print('The char of 1st idx from end: ' + name[-1])
print('The char of 2nd idx from end: ' + name[-2])

print(name[0:3]) #prints 0,1,2 th chars
print(name[0:]) #prints from 0 to end
print(name[:5]) #prints from 0 to 5
print(name[1:-1]) # from 1st char to the char  before -1(b)

#copying Strings ------->
copy_name = name[:]
print(copy_name)