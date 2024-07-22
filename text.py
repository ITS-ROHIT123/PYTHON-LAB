# Create and write to the file
with open("ABC.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Call the function to read and display the file content
read_and_display_file("ABC.txt")
