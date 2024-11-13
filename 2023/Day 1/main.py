def openFile():
    """ Reads in a file and returns a list of each line in the file
    """
    textInput = []
    # f = open("/workspace/advent-of-code/2023/Day 1/testinput.txt", "r")
    f = open("/workspace/advent-of-code/2023/Day 1/input.txt", "r")
    for x in f:
        textInput.append(x)
        # print(x)
    f.close()
    return textInput

def main():
    """ Main Method
    """
    calibVal = openFile() # The Calibration Value
    cleanCalib = [] # The Cleaned up calibration

    for line in calibVal:
        newLine = []
        for char in line:
            if char.isdigit():
                newLine.append(char)
        cleanCalib.append(int(str(newLine[0])+str(newLine[-1])))
    #print(cleanCalib)

    # Sum all the values of the new calibrated coordinates
    print(sum(cleanCalib))

main()
exit