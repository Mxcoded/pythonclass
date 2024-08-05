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
flight = Flight(5)

# List of people to be added to the flight
people = ["Harry", "Sheyi", "Kayode", "Daniel"]

people.sort()
# Try to add each person to the flight
for person in people:

    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully. \n")
    else:
        print(f"No available seat for {person} ! \n")


# class Room:
#     def __init__(self, roomno, duration):
#         self.roomno = roomno
#         self.duration = duration
#         self.guest=[]


#         def add_guest_to_room(self,guest):

#         def check_availability(self):
#             self.guest=guest
#             self.
#             return True


class Room:
    def __init__(self, roomno, max_duration):
        self.roomno = roomno

        self.max_duration = max_duration
        self.guest = []

    def add_guest_to_room(self, guest, stay_duration):
        if self.check_availability(stay_duration):
            self.guest.append({"name": guest, "stay_duration": stay_duration})
            return True
        else:
            return False

    def check_availability(self, stay_duration):
        # Check if the room is available for the requested stay duration
        if len(self.guest) == 0:
            return stay_duration <= self.max_duration
        return False

    def current_guest(self):
        if len(self.guest) > 0:
            return self.guest[0]
        else:
            return None


# Example usage:
room101 = Room(101, 6)  # Room 101 with a maximum stay duration of 5 days

# Check if the room is available and add a guest if it is
if room101.add_guest_to_room("John Doe", 3):
    print(f"Guest added: {room101.guest} \n")
else:
    print("Room is not available. \n")

# Try to add another guest
if room101.add_guest_to_room("Jane Smith", 2):
    print(f"Guest added: {room101.guest}")
else:
    print("Room is not available.")

# Output the current guest list
print(f"Current guests in room {room101.roomno}: {room101.guest}")


class Bible:
    def __init__(self, name, testament, book, chapter, verse):
        self.name = name
        self.testament = testament
        self.book = book
        self.chapter = chapter
        self.verse = verse

    def set_book(self, name, chapter, verse):
        self.book = name
        self.chapter = chapter
        self.verse = verse
        return self


# Usage
bible = Bible("NKJV", "Old Testament", "Exodus", 5, 1)
print(
    f"We are reading the book of {bible.book} today! Chapter {bible.chapter}, Verse {bible.verse} ~ {bible.name}. \n"
)
