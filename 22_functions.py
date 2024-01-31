def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome Home')

greet_user("Asadullah", "Galib")


###  KEYWOR ARGUMENTS  ###
def greet_admin(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome Home')

greet_admin(last_name="Galib", first_name="Asadullah") # In this case positioning of arguments doesnt matter


#   RETURN STATEMENTS   ###
def square(number):
    return number * number

print(square(3))