def probBySumGenerator(maxValue):
    
    masterTable = {} 

    def probBySumTable(numDice):
            
        if numDice == 1 and numDice not in masterTable:
            masterTable[1] = dict([(i, 1/float(maxValue)) for i in range(1, maxValue + 1)])
        elif numDice not in masterTable:
            table = {}
            for val in range(numDice, numDice*maxValue+1):
                valProb = 0
                for firstRoll in range(1, maxValue+1):
                    subTable = probBySumTable(numDice-1)
                    if (val - firstRoll) in subTable:
                        valProb += subTable[val - firstRoll] / float(maxValue)
                table[val] = valProb

            masterTable[numDice] = table
        
        return masterTable[numDice]

    return probBySumTable


pProbs = (probBySumGenerator(4))(9)
cProbs = (probBySumGenerator(6))(6)

# print pProbs
# print cProbs

probPWins = 0

for pVal in pProbs:
    for cVal in cProbs:
        if pVal > cVal:
            probPWins += pProbs[pVal] * cProbs[cVal]

print probPWins