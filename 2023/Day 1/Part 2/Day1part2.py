def openFile():
    """ Reads in a file and returns a list of each line in the file
    """
    textInput = []
    f = open("/workspace/advent-of-code/2023/Day 1/Part 2/part2TestInput.txt", "r")
    #f = open("/workspace/advent-of-code/2023/Day 1/Part 2/part2Input.txt", "r")
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
    digits = ['one','two','three','four','five','six','seven','eight','nine']
    notDigit = ""

    # Parse each line in the input
    for line in calibVal:
        cleanedLine = [] # Declare a list to hold the new, cleaned line
        
        # Parse each character in the line
        for char in line:    
            # If the character is a number, add it to the new clean line immediately
            if char.isdigit():
                cleanedLine.append(char)
                print("appending ", char)
                notDigit = "" # Reset the string for checking for spelled out numbers
            # If the character is NOT a number
            else:
                notDigit += char #Building a string of the characters to check if it spells out a number
                
                # Enumerate through the list of number strings, check if our string is in it
                for digit in digits: 
                    if notDigit.find(digit) > -1:
                        # print(notDigit.find(digit), digit, notDigit, sep=", ")
                        # print("appending ", digits.index(digit)+1)
                        
                        # Since the list of digits is in order, we can convert the number we found to an integer
                        # just by using the index + 1. Which we append to our new cleanedLine
                        cleanedLine.append(digits.index(digit)+1)
                        notDigit =str(char)

        cleanCalib.append(int(str(cleanedLine[0])+str(cleanedLine[-1])))
        # print(cleanCalib)
    print("Final cleaned calibration: ", cleanCalib, sep = '')

    # Sum all the values of the new calibrated coordinates
    print(sum(cleanCalib))

main()
exit