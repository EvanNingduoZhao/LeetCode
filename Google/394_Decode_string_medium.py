# 首先遇到括号套括号的问题就要能想到这题需要用recursion或者stack
# 我的写法是用的recursion，下面还会介绍一下stack的写法，但是可以发现
# stack的写法实际上是比较复杂不好写的，在面试中recursion的解法更好想，更好写

class Solution:
    def decodeString(self, s: str) -> str:
        # res就是我们最后要return的，我们在traverse s的过程中，把decode出来的内容
        # 不断的加到res上
        res = []
        i = 0
        while i <= len(s) - 1:
            # 从头到位开始traverse 如果遇到的不是数字，直接加到res上
            if s[i].isdigit() == False:
                res.append(s[i])
                i += 1
            # 如果是数字的话
            else:
                # 先用helper func parser数字，numEndIndex是数字后面的那个[]的content里的第一个字母的index
                # num是parse出来的数字
                numEndIndex, num = self.parseNum(i, s)
                # 之后用recursive function来parse这组数字和[]，已经[]里面可能有的nested的[]
                endIndex, product = self.parseBracket(numEndIndex, s, num)
                res.append(product)
                # 这一套结束以后i就等于这组数字和[]的最外层结尾括号后面的下一个char的index
                i = endIndex
        return "".join(res)

    def parseBracket(self, startIndex, s, multiplier):
        content = []
        i = startIndex
        # 这个while loop是go through[]里面的内容
        while i <= len(s) - 1 and s[i] != "]":
            # 如果这里又见到digit，说明存在[]里的nested[]
            if s[i].isdigit():
                numEndIndex, newMultiplier = self.parseNum(i, s)
                endIndex, product = self.parseBracket(numEndIndex, s, newMultiplier)
                i = endIndex
                content.append(product)
            else:
                content.append(s[i])
                i += 1
        # 这里i还是指向后]的index，给i再加1，让他指向]之后的第一个char的index
        i += 1
        return i, "".join(content) * multiplier

    # parseNum是一个helper function，它的作用是比如在index i遇到一个digit char时，
    # call parserNum，它负责向后查看i后面的char，看它们是不是digit char，如果是的话
    # 把它们一个一个都收集起来，之后return数字后面的那个[]的content里的第一个字母的index，和
    # parse出来并已经被转化成int的这个遇到的数字
    # 对于这种小task 一定要写helper function，代表着好的习惯，也给自己减少很多headache
    def parseNum(self, startIndex, s):
        i = startIndex
        num = []
        while s[i].isdigit():
            num.append(s[i])
            i += 1
        return i + 1, int("".join(num))