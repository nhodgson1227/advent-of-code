import re

def openFile():
    """
    """
    f = open("/workspace/advent-of-code/2024/Day3/Part2/testinput.txt", "r")
    fileInput = f.read()
    f.close()
    return fileInput

# Test Input    
#txt = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
txt = openFile()

# Split the string int
txt = re.split(r"do\(\)", txt)
for i in range(len(txt)):
    txt[i] = re.sub(r"don't\(\).*", "",txt[i])
txt = list(filter(None, txt))

sumMult = 0
# Parse and clean instructions from the new input list
for instr in txt:
    validInstr = re.findall(r"mul\(\d*,\d*\)", instr)
    for i in range(len(validInstr)):
        validInstr[i] = validInstr[i].strip("mul(").strip(")").split(",")


    for instruction in validInstr:
        sumMult += int(instruction[0]) * int(instruction[1])

print(sumMult)