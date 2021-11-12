str="0001010111"

def flipCoin(str):
    # Compare the number of flips required to obtain a binary string alternate that starts with '01'
    # with that required to obtain a binary string alternate that starts with '10'. Then, return the smaller one.
    return min(getFlipCount(str,'0'),getFlipCount(str,'1'))

def getFlipCount(str,start):
    count=0
    for char in str:
        if char != start:
            count+=1
        if start=='0':
            start='1'
        else:
            start='0'
    return count


print(getFlipCount(str,'0'))
print(getFlipCount(str,'1'))
print(flipCoin(str))