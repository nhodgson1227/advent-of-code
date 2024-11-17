def openFile():
    """ Reads in a file and returns a list of each line in the file
    """
    textInput = []
    #f = open("/workspace/advent-of-code/2023/Day 2/Part 1/testinput.txt", "r")
    f = open("/workspace/advent-of-code/2023/Day 2/Part 1/input.txt", "r")
    for x in f:
        textInput.append(x.rstrip()) # rstrip = Remove trailing newline
        # print(x)
    f.close()
    return textInput

def checkGame(game):
    """ Takes the list of games, returns the lowest poassible values 
    """
    gameLimit= [0,0,0] # records the highest value for each hand
    # Split the game by hands
    for i in game.split(";"):
        #print("Hand: ", i)
        parsedHand = [0,0,0] # Create/reset a new blank hand
        numCube = 0 # Create/reset numCube if the split element isn't a color string, then it is the number of cubes, so we store that value

        # Split the hand into elements, strip the commas. If the value is a number, save it, if it's a color, add the previous number to the total
        # This part ain't pretty but it works
        for x in i.split():
            x = x.strip(",")
            if x == 'red':
                parsedHand[0] += numCube
            elif x =='green':
                parsedHand[1] += numCube
            elif x =='blue':
                parsedHand[2] += numCube
            else: 
                numCube = int(x)

        for z in range(3):
            if (parsedHand[z] > gameLimit[z]):
                gameLimit[z] = parsedHand[z]

    return gameLimit


def main():
    """ Main Method
    """
    gamePower = 0
    gameInput = openFile()

    for game in gameInput:
        # print("Line to Parse:", game)
        gameNum = int(game.split(":",1)[0][4:]) # Grabs the game number
        game = game[game.find(":")+2:] # Removes the 'Game: ' from the input
        power = 1
        for g in checkGame(game):
            power *= g
        gamePower += power
    print(gamePower)
main()
exit