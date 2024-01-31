try:
    age = int(input("Enter Your Age: ")) # if we dont input an integer then we will get exception
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be 0')
except ValueError:
    print("Invalid value")