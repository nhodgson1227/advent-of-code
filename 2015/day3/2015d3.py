def openFile():
    # Open the file in read mode
    file = open('/workspace/advent-of-code/2015/day3/input.txt', 'r')
    directions = file.read()
    file.close()
    return directions

directions = openFile()
#directions = '^>v<^>v<'
currentPos = [0,0]
presents = {}

for _dir in directions:
    if _dir == '^':
        currentPos[1] += 1
    elif _dir == '>':
        currentPos[0] += 1
    elif _dir == '<':
        currentPos[0] -= 1
    elif _dir == 'v':
        currentPos[1] -= 1
    else:
        print("Input error. Please check for valid input")
    
    # Check if the coordinates have been visited and increment a present delivered. If not, set them to 1 present delivered.
    try:
        presents[currentPos[0],currentPos[1]]
    except:
        presents[currentPos[0],currentPos[1]] = 1
    else:
        presents[currentPos[0],currentPos[1]] += 1

print(len(presents))