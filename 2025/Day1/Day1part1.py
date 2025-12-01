def read_file():
    fileInput = []
    #f = open("2025/Day1/testinput.txt", "r")
    f = open("2025/Day1/input.txt", "r")
    for line in f:
        fileInput.append(line)
    f.close()
    return fileInput

def main():
    """ Main Method
    """
    rotationInstructions = read_file()
    sequence = 0
    dial = 50

    for instruction in rotationInstructions:
        if instruction[0]  == 'L':
            dial -= int(instruction[1:])
            while dial < 0:
                dial += 100
        elif instruction[0] == 'R':
            dial += int(instruction[1:])
            while dial >= 100:
                dial -= 100
        #print("Dial now at: " + str(dial))
        if dial == 0:
            sequence += 1
    print("Sequence number is: ", sequence)
# MAIN CALL
main()
exit