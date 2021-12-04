# 研究官方solution
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        bullIndex = set()
        noneBullMap = {}
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                bullIndex.add(i)
            else:
                if secret[i] in noneBullMap:
                    noneBullMap[secret[i]]+=1
                else:
                    noneBullMap[secret[i]]=1
        for i in range(len(guess)):
            if i not in bullIndex:
                if guess[i] in noneBullMap and noneBullMap[guess[i]]!=0:
                    noneBullMap[guess[i]]-=1
                    cows+=1
        return str(bulls)+"A"+str(cows)+"B"