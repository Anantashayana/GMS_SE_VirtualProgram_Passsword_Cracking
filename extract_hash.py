# Open the file in read mode
with open('./hash.txt', 'r') as file:
    # Read all the lines in the file
    lines = file.readlines()

# Open the file in write mode
with open('./hash1.txt', 'w') as file:
    # Loop through each line in the lines list
    for line in lines:
        # Find the index of the ':' character in the line
        index = line.find(':')
        # Write the substring after ':' character to the file
        file.write(line[index+1:])