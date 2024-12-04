def main():
    """ Main Method
    """
    firstList = []
    secondList = []
    simScore = []

    # Open the file, split the input into the lists
    #f = open("/workspace/advent-of-code/2024/Day1/Part2/testinput.txt", "r")
    f = open("/workspace/advent-of-code/2024/Day1/Part2/input.txt", "r")
    for line in f:
        # Input is split by 3 spaces, strip out newline
        line = line.strip().split("   ")
        firstList.append(int(line[0]))
        secondList.append(int(line[-1]))
    f.close()

    # Sort the lists
    firstList.sort()
    secondList.sort()

    # Take the difference between each element in both lists and add it together:
    for i in range(len(firstList)):
        #print(secondList.count(firstList[i]))
        simScore.append(int(firstList[i]) * secondList.count(firstList[i]))
    print(sum(simScore))
# MAIN CALL
main()
exit