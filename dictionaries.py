# Dictionary in Python is like a list, however, it takes in two arguments: what you are looking up and the value
state = {"Sheyi": "Osun", "Kayode": "Kwara", "Samuel": "Enugu"}

name = input("What's your Name?: ")

# Check if the name is empty or not in the dictionary
if not name:
    print("You didn't enter a name.")
elif name not in state:
    state[name] = "Osun"  # Assign a default state if the name is not found

# Look up the value of the given name in the dictionary
print(
    f"Your name is {name}. From my dictionary, you are from {state[name]} State, Nigeria!"
)
