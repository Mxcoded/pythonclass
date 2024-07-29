# List on names, this is list syntax
names = ["Harry", "Jerry", "Solomon", "Samsudeen", "Juwon", "Kayode", "Samuel"]
for name in names:
    names.sort()
    print(name)
# Testing For statement with python built in function @range"
n = range(10)
for i in n:
    print(i)
# Looping through each character a user enter
user = input("Name: ")
for character in user:
    print(f"{user},\n {character}")
# looping through each character of the initial object of the list.
for character in names[0]:
    print(character)
