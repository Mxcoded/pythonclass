class Point:
    def __init__(self, input1, input2):
        """Initialize a new Point with coordinates x and y."""
        self.x = input1
        self.y = input2


# Create an instance of Point with coordinates (4, 8)
p = Point(4, 8)

# Print the x coordinate of the Point instance
print(p.x)

# Print the y coordinate of the Point instance
print(p.y)


class Flight:
    def __init__(self, capacity):
        """Initialize a new Flight with a given capacity."""
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        """
        Add a passenger to the flight if there are open seats.
        Returns True if successful, False otherwise.
        """
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        """Return the number of open seats on the flight."""
        return self.capacity - len(self.passengers)


# Create an instance of Flight with a capacity of 3
flight = Flight(3)

# List of people to be added to the flight
people = ["Harry", "Sheyi", "Kayode", "Daniel"]


# Try to add each person to the flight
for person in people:
    people.sort()
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seat for {person}")


class Room:
    def __init__(self, roomno, duration):
        self.roomno = roomno
        self.duration = duration
        self.guest=[]
        self.booking=[]

        def add_guest_to_room(self,guest,boking):
            