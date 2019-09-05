maxTerm = 4000000

previousTerm = 0
currentTerm = 1

total = 0
while (currentTerm + previousTerm) < maxTerm:
    tmpPreviousTerm = currentTerm
    currentTerm = previousTerm + currentTerm
    previousTerm = tmpPreviousTerm
    if currentTerm % 2 == 0:
        total += currentTerm

print('Total: ', total)
