def frequency(s):
    stack = []
    res = [0]*26
    i = 0
    # 我们总体的策略是一个一个把遇到的char往一个stack里push
    while i < len(s):
        # 让遇到了一个#时，说明之前push进去的两个数字应该被当作一个两位数
        # 那么我们从stack里连续pop出来个char
        if s[i] == "#":
            print("encountered #, stack is:", stack)
            d1 = stack.pop()
            d2 = stack.pop()
            index = int(d2)*10+int(d1)
            print("index is:", index)
            # 这时我们还要check一下#后面是不是一个（
            # 当然必须i+1<len(s)才保证#后面还有东西
            if i+1<len(s):
                # 如果#后面是（，那么把括号里的数字读出来
                if s[i+1]=="(":
                    i+=2
                    count = []
                    while s[i]!=")":
                        count.append(s[i])
                        i+=1
                    # 在res里相应的index对应的element上加上括号里读出来的数字
                    res[index-1]+=int("".join(count))
                # 如果#后面不是（，那么直接在res里相应的index对应的element上加上1
                else:
                    res[index-1]+=1
                    print("res is:", res)
            # 如果#就是s的最后一个char了的话，那么也直接在res里相应的index对应的element上加上1
            else:
                res[index - 1] += 1
        # 如果在traverse s时，直接就遇到了一个（，即不是在#后面的（
        # 那么这个括号里的count肯定就是给括号前面那一位数字对应的字母的
        elif s[i] == '(':
            # 所以pop出前一位数字，读出括号里的count，在res里相应的index对应的element上加上括号里读出来的数字
            index = int(stack.pop())
            i += 1
            count = []
            while s[i] != ")":
                count.append(s[i])
                i += 1
            res[index - 1] += int("".join(count))
        # 如果当前的s[i]就是一个数字的话，就直接push到stack上
        else:
            stack.append(s[i])
        # 要记得+1保持while loop的运转
        i+=1
    # 最后stack上剩下的都是一位数字代表一个字母且在s里后面没有跟着括号的，
    # 所以一个一个pop出来 转化成index 之后在res里相应的index对应的element上加上1
    while stack:
        index = int(stack.pop())
        res[index-1]+=1
    return res

s="23#(2)24#25#26#23#(3)"
print(frequency(s))