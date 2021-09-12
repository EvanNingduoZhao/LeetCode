def caesar_cipher(strings):
    orderDiffDict={}
    for s in strings:
        order = []
        for i in range(1,len(s)):
            diff = ord(s[i])-ord(s[i-1])
            order.append(str(diff))
        orderString = ''.join(order)
        if orderString not in orderDiffDict:
            orderDiffDict[orderString] = [s]
        else:
            orderDiffDict[orderString].append(s)
    res = []
    for k,v in orderDiffDict.items():
        res.append(v)
    return res

strings=['abc','bcd','acd','dfg']
print(caesar_cipher(strings))