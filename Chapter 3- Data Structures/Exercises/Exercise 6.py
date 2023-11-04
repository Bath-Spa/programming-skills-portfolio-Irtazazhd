# Create a list of people to invite to dinner
guests = ["Abdu", "cafeteria", "Topper", "Irti"]

# Print a message that you can only invite two people
print("Unfortunately, the dinner table won't arrive in time, so I can only invite two people for dinner.")

# Use pop() to remove guests and apologize to those who can't come
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner this time.")

# Print a message to the two people still on your list
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner.")

# Use del to remove the last two names and make the list empty
del guests[:]

# Print the list to ensure it's empty
print("The guest list is now empty:", guests)
