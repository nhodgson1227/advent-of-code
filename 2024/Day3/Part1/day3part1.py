import re

def openFile():
    """
    """
    #txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    f = open("/workspace/advent-of-code/2024/Day3/Part1/input.txt", "r")
    fileInput = f.read()
    f.close()
    return fileInput

txt = openFile()

validInstr = re.findall(r"mul\(\d*,\d*\)", txt)
for i in range(len(validInstr)):
    validInstr[i] = validInstr[i].strip("mul(").strip(")").split(",")

sumMult = 0
for instruction in validInstr:
    sumMult += int(instruction[0]) * int(instruction[1])

print(sumMult)