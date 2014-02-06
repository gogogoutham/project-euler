import math

def probOutcomeGenerator() :

    cache = {}
 
    def po(numBlue, numTotal):
        #print numBlue, numTotal
        if numBlue < 0 or numTotal <= 0 or numBlue > numTotal:
            return float(0)
        elif numTotal == 1:
            return .5
        elif "{0},{1}".format(numBlue, numTotal) not in cache:
            cache["{0},{1}".format(numBlue, numTotal)] = float(po(numBlue-1,numTotal-1))/float(numTotal+1) + float(po(numBlue, numTotal-1))*float(numTotal)/float(numTotal+1)
        return cache["{0},{1}".format(numBlue, numTotal)]

    return po

probOutcome = probOutcomeGenerator()

numTurns = 15

totalProb = 0
for numBlue in range(numTurns/2+1, numTurns+1):
    totalProb += probOutcome(numBlue, numTurns)

print totalProb
print math.floor(float(1-totalProb)/totalProb)