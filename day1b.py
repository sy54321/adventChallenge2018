import os
dataFile = 'dataDay1.txt'
currentFrequency = 0
seenFrequencies = []
with open(dataFile, 'r') as file:
    for line in file:
        if int(line) in seenFrequencies:
            print(f'This frequency has been seen already - here is the answer: {int(line)}')
            break
        seenFrequencies.append(int(line))
        currentFrequency += int(line)
