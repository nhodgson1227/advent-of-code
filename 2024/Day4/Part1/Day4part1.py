def openFile():
    """
    Opens the file and return a string containing the full input
    """
    f = open("/workspace/advent-of-code/2024/Day4/Part1/testinput.txt", "r")
    #f = open("/workspace/advent-of-code/2024/Day4/Part1/input.txt", "r")
    fileInput = f.read()
    f.close()
    return fileInput

def string_to_2d_array(input_string):
    # Split the string by newline characters to create rows
    rows = input_string.split('\n')
    # Convert each row into a list of characters
    array_2d = [list(row) for row in rows]
    return array_2d

def printArray(array):
    """
    Prints out a 2d array in a readable format
    """
    for row in array:
        print(row)

def check(x,y):
    # Check horizontal
    
    pass


def main():
    """ Main Method
    """
    wordSearch = string_to_2d_array(openFile())
    sizeX = len(wordSearch[0])
    sizeY = len(wordSearch)
    matches = 0

    for y in range(sizeY):
        for x in range(sizeX):
            if wordSearch[x][y] == 'X':
                matches += check(x,y)
    print("The total number of matches is: ", matches)

# MAIN CALL
main()
exit