first = 'Asadullah'
last = 'Galib'
#print like this -> Asadullah [Galib] is a coder---->
message = first + ' [' + last +'] is a coder'
print(message)
# BUT......this is not good approach. Understanding the code is difficult like this

opt_message = f'{first} [{last}] is a coder'
print(opt_message)