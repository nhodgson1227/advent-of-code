# Open the file in read mode
file = open('/workspace/advent-of-code/2015/day1/input.txt', 'r')
floor = 0
position = 1

while True:
    char = file.read(1)

    if not char:
        break
    
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    else:
        print("Incorrect character detected");
        break
    
    if floor == -1:
        print("Basement at: ", position)
        position += 1
    else:
        position += 1

print("The correct floor is: ", floor)
# Close the file
file.close()


