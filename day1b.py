import os
dataFile = 'dataDay1.txt'
currentFrequency = 0
seenFrequencies = []
foundMatch = False
def checkData():
    global currentFrequency
    global seenFrequencies
    global foundMatch
    if len(seenFrequencies)%5 == 0:
        print(f'The program has checked {len(seenFrequencies)} frequencies.')
    with open(dataFile, 'r') as file:
        for line in file:
            seenFrequencies.append(currentFrequency)
            currentFrequency += int(line)
            if currentFrequency in seenFrequencies:
                print(f'This frequency has been seen already - here is the answer: {currentFrequency}')
                print(f'The program checked {len(seenFrequencies)} frequencies.')
                foundMatch = True
                break
            #print(seenFrequencies)

while foundMatch == False:
    checkData()

print('Program Complete')