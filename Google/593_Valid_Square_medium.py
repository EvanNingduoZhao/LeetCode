class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def getDistance(p1,p2):
            return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        if p1[0]==p2[0] and p1[1]==p2[1] and p1[0]==p3[0] and p1[1]==p3[1] and p1[0]==p4[0] and p1[1]==p4[1]:
            return False
        else:
            pointsList = [p1,p2,p3,p4]
            distances = [0 for _ in range(3)]
            distances[0]=getDistance(p1,p2)
            distances[1]=getDistance(p1,p3)
            distances[2]=getDistance(p1,p4)
            maxDistance = max(distances)
            nonDiagonal = []
            diagonal=0
            for i in range(3):
                if distances[i]!=maxDistance:
                    nonDiagonal.append(i)
                else:
                    diagonal=i
            if len(nonDiagonal)!=2:
                return False
            if distances[nonDiagonal[0]]==distances[nonDiagonal[1]] and distances[nonDiagonal[0]]*2==maxDistance:
                if getDistance(pointsList[nonDiagonal[0]+1],pointsList[nonDiagonal[1]+1])==maxDistance:
                    startToNonDiagonal = getDistance(p1,pointsList[nonDiagonal[0]+1])
                    diagonalToNonDiagonal1 = getDistance(pointsList[diagonal+1],pointsList[nonDiagonal[0]+1])
                    diagonalToNonDiagonal2 = getDistance(pointsList[diagonal+1],pointsList[nonDiagonal[1]+1])
                    if startToNonDiagonal == diagonalToNonDiagonal1 and startToNonDiagonal == diagonalToNonDiagonal2:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def getDistance(p1,p2):
            return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        pointLists = [p1,p2,p3,p4]
        pointLists.sort(key = lambda x:(x[0],x[1]))
        p1=pointLists[0]
        p2=pointLists[1]
        p3=pointLists[2]
        p4=pointLists[3]
        e1 = getDistance(p1,p3)
        e2 = getDistance(p1,p2)
        e3 = getDistance(p2,p4)
        e4 = getDistance(p3,p4)
        d1 = getDistance(p1,p4)
        d2 = getDistance(p2,p3)
        if p1==p2 and p1==p3 and p1==p4:
            return False
        if e1==e2 and e1==e3 and e1==e4 and d1==d2:
            return True
        else:
            return False