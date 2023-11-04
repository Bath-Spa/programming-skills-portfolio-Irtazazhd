# Define the cost of a single USB stick and the girl's budget
usb_stick_price = 6
budget = 50

# Calculate how many USB sticks she can buy
usb_sticks_purchased = budget // usb_stick_price

# Calculate how much money she will have left
remaining_money = budget % usb_stick_price

# Print the results
print(f"She can buy {usb_sticks_purchased} USB sticks.")
print(f"She will have £{remaining_money} left.")