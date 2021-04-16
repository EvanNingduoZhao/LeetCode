def deleteToNoConsecutive3(s):
    if not s or len(s)<3:
        return s
    chars=[]
    counter=0
    lastChar=None
    for char in s:
        if lastChar==None:
            lastChar=char
            counter=1
            chars.append(char)
        else:
            if char==lastChar:
               if counter<2:
                   counter+=1
                   chars.append(char)
               else:
                   continue
            else:
                chars.append(char)
                lastChar=char
                counter=1
    return ''.join(chars)
print(deleteToNoConsecutive3('eedaaad'))
print(deleteToNoConsecutive3('xxxtxxx'))
print(deleteToNoConsecutive3('uuuuxaaaaxuuu'))
