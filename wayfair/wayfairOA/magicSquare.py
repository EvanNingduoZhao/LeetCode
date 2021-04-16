def magicSquare(matrix):
    N=len(matrix)
    M=len(matrix[0])
    maxD=1
    for i in range(N-1):
        for j in range(M-1):
            print()
            print("start point is: ",matrix[i][j])
            isMagic=True
            d=2
            while i+(d-1)<=N-1 and j+(d-1)<=M-1:
                print("dimension this time is: ",d)
                target=None
                # check if row sums equal to target
                for row in range(d):
                    rowSum=0
                    for c in range(d):
                        rowSum+=matrix[i+row][j+c]
                    print("rowSum is: ",rowSum)
                    if not target:
                        target=rowSum
                        print("target becomes: ",target)
                    else:
                        if rowSum!=target:
                            isMagic=False
                            break
                    if isMagic==False:
                        break
                if isMagic==False:
                    d+=1
                    isMagic = True
                    continue

                # check if col sums equal to target
                for col in range(d):
                    colSum=0
                    for r in range(d):
                        colSum+=matrix[i+r][j+col]
                    print("colSum is: ", colSum)
                    if colSum!=target:
                        isMagic=False
                        break
                if isMagic==False:
                    d+=1
                    isMagic = True
                    continue

                # check if two diagnol sums equal to target
                diagSum1=0
                for k in range(d):
                    diagSum1+=matrix[i+k][j+k]
                print("diagSum1 is: ", diagSum1)
                if diagSum1!=target:
                    d+=1
                    isMagic = True
                    continue
                diagSum2=0
                for k in range(d):
                    diagSum2+=matrix[i+d-1-k][j+d-1-k]
                print("diagSum2 is: ", diagSum2)
                if diagSum2!=target:
                    d+=1
                    isMagic = True
                    continue

                maxD=max(maxD,d)
                print("maxD becomes:",maxD)
                d+=1
                isMagic = True
    return maxD


matrix=[[7,2,4],
        [2,7,6],
        [9,5,1],
        [4,3,8],
        [3,5,4]]

print(magicSquare(matrix))
