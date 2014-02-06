import math

def probYWinsGenerator() :
    
    pywCache = {}

    def pyw(pntwx, pntwy):

        if pntwy <= 0:
            return float(1)
        elif pntwx <= 0:
            return float(0)
        elif "{0},{1}".format(pntwx, pntwy) in pywCache:
            return pywCache["{0},{1}".format(pntwx, pntwy)]

        pywVal = 0
        for t in range(1, int(math.ceil(math.log(pntwy,2))+2)):
            # Non - Solving Recursion
            # probWinningForT = 
            #     1/pow(2,t)*( # Successful at getting payout
            #         .5*pyw(pntwx-1, pntwy - pow(2,t-1)) + # Player x gets a point
            #         .5*pyw(pntwx, pntwy - pow(2,t-1)) # Player x doesn't get a point
            #     ) + 
            #     (pow(2,t)-1)/pow(2,t)*( # Unsuccessful at getting payout
            #         .5*pyw(pntwx-1, pntwy) + # Player x gets a point
            #         .5*pyw(pntwx, pntwy) # Player x doesn't get a point
            #     )

            # Solving Recursion
            probWinningForT = (pow(2,t+1) / float(pow(2,t) + 1))*(
            float(1)/pow(2,t)*( # Successful at getting payout
                .5*pyw(pntwx-1, pntwy - pow(2,t-1)) + # Player x gets a point
                .5*pyw(pntwx, pntwy - pow(2,t-1)) # Player x doesn't get a point
            ) + 
            float(pow(2,t)-1)/pow(2,t)*( # Unsuccessful at getting payout
                .5*pyw(pntwx-1, pntwy) # Player x gets a point
            ))

            pywVal = max(pywVal, probWinningForT)

        pywCache["{0},{1}".format(pntwx, pntwy)] = pywVal
        return pywCache["{0},{1}".format(pntwx, pntwy)]
    
    return pyw

probYWins = probYWinsGenerator()

print .5*probYWins(100,100) + .5*probYWins(99,100)