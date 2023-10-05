import math

# Get the radius of the circle from the user
radius_str = input("Enter the radius of the circle: ")

# Convert the input string to a floating-point number
radius = float(radius_str)

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Display the result
print(f"The area of the circle with radius {radius} is {area:.2f}")
