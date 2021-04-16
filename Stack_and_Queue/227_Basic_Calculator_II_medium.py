# 这道题最重要的部分就是order precedence。要看明白一个问题，即我现在看了一个数，一个数后面的operator
# 以及operator再后面的那个数。我怎么能确定我现在能不能直接算这两个数用这个operator的结果？
# 如果这个operator是*或者/那可以直接算，但是如果是+或者-，那就得看下一个operator是什么
# 假设我们现在遇到的算式是 3-4*5/2+7
class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        operators = ['+','*','/','-']
        stack = []
        currNumList = []
        # 上一个见到的operator存在这，之所以初始值是+，是因为碰到第一个operator时
        # 我们要直接把它前面的第一个数放到stack里，而从下面的第22行可以看到，lastOperation
        # 是+时，直接把前面的数放进stack里
        lastOperation = "+"
        for i in range(len(s)):
            c = s[i]
            if c.isnumeric():
                currNumList.append(c)
            # 当我们见到了一个新的operator或者走到了s的结尾时，标志着我们看完了一个数字
            # （因为数字有可能是很多位的）
            if c in operators or i==len(s)-1:
                newNum = int(''.join(currNumList))
                currNumList = []
                # 上一个见到的operator是+或者-的话，不能直接进行计算，而是要存到stack里最后一起算
                if lastOperation=='+':
                    stack.append(newNum)
                # 为了避免我们最后一起算的时候还要区分当初是要加还是减，如果上一个见到的是-的话
                # 那么我们把新数字的相反数存到stack里，这样最后在stack里我们就可以都按照加来算
                # 按照上面的例子算式，当我们c走到*时，lastOperation是-，所以我们把-4放到stack里
                # 等我们c走到/时我们发现lastOperation是*，那么我们就把-4从stack里pop出来，和5乘
                # 在一起。如果假设我们的算式是3-4+5/2+7，那么走到/时发现last operation是+
                # 这样的话我们暂时不会对-4做什么了，它会一直留在stack里最后和其他留在stack里的
                # 一起加和得到结果
                elif lastOperation=='-':
                    stack.append(-newNum)
                # 当上一个见到的operator是*或者/的时候，直接计算上一个operator
                # 左右两个数字的*或者/的结果，之后把结果push到stack里
                elif lastOperation=='*':
                    stack.append(newNum*stack.pop())
                else:
                    stack.append(int(stack.pop()/newNum))
                # 把上一次见到的operator更新成刚见到的这个operator
                lastOperation = c
        # 其实整个思路相当于把每个不是加法的运算都转化乘加法，之后最后把所有的加数sum起来
        # 减法转加法的思路上面说了，对于乘和除我们是把结果算出来，之后把结果push到stack里作为加数
        return sum(stack)



#     下面的方法去掉了stack，是一个time O(n) space O(1)的解法
# 假设算式还是5*3-4*5/2+7
class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        operators = ['+','*','/','-']
        result = 0
        lastNumber = 0
        currNumList = []
        lastOperation = "+"
        for i in range(len(s)):
            c = s[i]
            if c.isnumeric():
                currNumList.append(c)
            if c in operators or i==len(s)-1:
                newNum = int(''.join(currNumList))
                currNumList = []
                if lastOperation=='+':
                    # 当c走到第二个*时，-4是要怎么参与运算还不确定
                    # 但是这时5*3已经算出来被存到lastNumber里了
                    # 我们把5*3的结果加到result上
                    result += lastNumber
                    lastNumber = newNum
                elif lastOperation=='-':
                    result += lastNumber
                    lastNumber = -newNum
                # 这种方法其实还是使用上面说的把所有运算都转化乘加法的原则
                # 只不过不是都转化好了最后一起加起来，而是转化好一个加在result上一个
                # 对于一个乘除运算或者连着一串乘除运算，我们的目的是把它们的结果算出来
                # 最后作为一个单独的加数加到result上。那么一串乘除计算的结束的标志就是
                # 看到了一个新的+或者-，且看到新的+或-时，一串乘除的结果已经算好存在lastNumber里了
                elif lastOperation=='*':
                    lastNumber = newNum*lastNumber
                else:
                    lastNumber= int(lastNumber/newNum)
                lastOperation = c
        # 把最后一个lastNumber加到result上之后return
        result += lastNumber
        return result