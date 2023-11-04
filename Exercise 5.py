# Create a list of people to invite to dinner
guests = ["Abdu", "Topper", "Cafeteria"]

# Print the name of the guest who can't make it
guest_cant_make_it = "Taha"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.")

# Replace the guest who can't make it with a new person
new_guest = "Irti"
guests.remove(guest_cant_make_it)
guests.append(new_guest)

# Print a second set of invitation messages
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to a dinner at my place. It would be an honor to have you join us.")