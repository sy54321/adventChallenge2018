import os
import numpy
dataFile = 'dataDay1.txt'
currentFrequency = 0
with open(dataFile, 'r') as file:
    for line in file:
        currentFrequency += int(line)
print(currentFrequency)
