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

# strings=['abc','bcd','acd','dfg']
# print(caesar_cipher(strings))

def caesar_cipher_2(s,k):
    res = []
    for char in s:
        asciiCode = ord(char)-k
        if asciiCode<ord('A'):
            asciiCode=ord("Z")+1-(ord('A')-asciiCode)
        res.append(chr(asciiCode))
    return ''.join(res)

print(caesar_cipher_2("VTAOG",2))