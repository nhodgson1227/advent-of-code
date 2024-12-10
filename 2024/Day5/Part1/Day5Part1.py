def openFile():
    """
    Opens the file and return a string containing the full input
    """
    f = open("/workspace/advent-of-code/2024/Day5/Part1/testinput.txt", "r")
    #f = open("/workspace/advent-of-code/2024/Day5/Part1/input.txt", "r")
    fileInput = f.read()
    f.close()
    return fileInput
