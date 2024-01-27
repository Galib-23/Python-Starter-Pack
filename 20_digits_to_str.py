phone = input("phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " " # "!" is default value. If any key is not present then it shows up.
    # here we could also use digits_mapping[ch]
print(output)