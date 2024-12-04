def main():
    """ Main Method
    """
    firstList = []
    secondList = []
    diffSum = 0

    # Open the file, split the input into the lists
    #f = open("/workspace/advent-of-code/2024/Day1/Part1/testinput.txt", "r")
    f = open("/workspace/advent-of-code/2024/Day1/Part1/input.txt", "r")
    for line in f:
        # Input is split by 3 spaces, strip out newline
        line = line.strip().split("   ")
        firstList.append(line[0])
        secondList.append(line[-1])
    f.close()

    # Sort the lists
    firstList.sort()
    secondList.sort()

    # Take the difference between each element in both lists and add it together:
    for i in range(len(firstList)):
        diffSum += abs(int(firstList[i])-int(secondList[i]))
        # print(diffSum, abs(int(firstList[i])-int(secondList[i])))

    print("The final sum is: ", diffSum)

# MAIN CALL
main()
exit