# Open the file in read mode
file = open('/workspace/advent-of-code/2015/day2/input.txt', 'r')
sqrft = 0
ribbon = 0
for line in file:
    # Throw the dimensions in a list and convert to integers
    dim = line.strip().split("x")
    dim = [int(x) for x in dim]

    sqrft += (2*dim[0]*dim[1]) + (2 * dim[1] * dim[2]) + (2 * dim[2] * dim[0])
    sqrft += min(dim[0]*dim[1], dim[1] * dim[2], dim[2] * dim[0])
    # Calculate ribbon
    x = sorted(dim)[:2]
    ribbon += x[0] + x[0] + x[1] + x[1]
    # Tie the bow
    ribbon += dim[0] * dim[1] * dim[2]

print(sqrft)
print(ribbon)
# Close the file
file.close()


