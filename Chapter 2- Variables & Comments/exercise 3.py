# Define a name with leading and trailing whitespace characters
name = "\t\n   Muhammad Faseeh   \t\n"

# Print the name with surrounding whitespace
print("Original Name:")
print(name)

# Strip and print the name using lstrip(), rstrip(), and strip()
print("\nAfter Stripping:")
print("Using lstrip():", name.lstrip())
print("Using rstrip():", name.rstrip())
print("Using strip():",name.strip())