def openFile():
    """ Reads in a file and returns a list of integer listsSplit by spaces, strip of newline
    # Parse through the list of strings, convert to a list of integers
    # Return a list of iteger lists.
    """
    fileInput = []

    # Open the file


    f = open("/workspace/advent-of-code/2024/Day2/Part1/testinput.txt", "r")
    #f = open("/workspace/advent-of-code/2024/Day2/Part1/input.txt", "r")
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
    # Check if levels are decreasing or increasing by
    # sorting the report into ascending and descending lists and check if the original matches either
    reportInc = report.copy()
    reportDec = report.copy()
    reportDec.sort(reverse=True)
    reportInc.sort()
    
    if (report != reportDec) and (report != reportInc):
        #print("Levels are not all increasing or all decreasing")
        #print(report, reportInc, reportDec)
        return False

    # Now we check that each step is within the correct range
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff > stepMax or diff < stepMin:
            #print("Out of step range. ", diff, diff > stepMax, diff < stepMin)
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
        if checkSafety(report,stepMin, stepMax):
            safeCount += 1
    print(safeCount)

### --- MAIN CALL --- ###
main()
exit