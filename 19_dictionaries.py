# DICTIONARY is a key-value pair. Keys 
person = {
    "name": "Galib",
    "age": 22,
    "salary": 10,
    "salary": 20  #salary will be printed only once. Because dictionary only consists of single key
                  # Also latest salary value --->>> "salary": 20 will be printed.
}
print(person) 

print(person["age"])