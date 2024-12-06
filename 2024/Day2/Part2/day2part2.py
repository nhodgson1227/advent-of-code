def openFile():
    """ Reads in a file and returns a list of integer listsSplit by spaces, strip of newline
    # Parse through the list of strings, convert to a list of integers
    # Return a list of iteger lists.
    """
    fileInput = []

    # Open the file

    f = open("/workspace/advent-of-code/2024/Day2/Part2/testinput.txt", "r")
    #f = open("/workspace/advent-of-code/2024/Day2/Part2/input.txt", "r")
    for line in f:
        line = line.strip().split(" ")
        lineInt = []
        for item in line:
            lineInt.append(int(item))
        fileInput.append(lineInt)
        # Input is split by 1 spaces, strip out newline
    f.close()
    return fileInput

def checkSafety(report,stepMin,stepMax):
    """
    """
    print(report)
    if recur > 1:
        recur = 0
        return False
    # Check if levels are decreasing or increasing
    # Decreasing
    if report[0] > report[-1]:
        for i in range(len(report)-1):
            if report[i] < report[i+1]:
                #report.remove(report[i+1])
    # Increasing
    elif report[0] < report[-1]:
        pass
    else:
        pass


    # Now we check that each step is within the correct range
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff > stepMax or diff < stepMin:
            #report.remove(report[i+1])
            return False
    return True

### --- MAIN --- ###
def main():
    """ Main Method
    """
    stepMin = 1
    stepMax = 3
    safeCount = 0
    reports = openFile()
    for report in reports:
        recur = 0
        if checkSafety(report,stepMin, stepMax):
            safeCount += 1
    print(safeCount)

### --- MAIN CALL --- ###
main()
exit