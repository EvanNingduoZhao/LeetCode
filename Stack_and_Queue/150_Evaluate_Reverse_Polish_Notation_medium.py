#这道题属于典型用stack解决的问题，下面用一个复杂一些的test case来说明这个题里比较tricky的地方
#["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#对于某一个operand而言，它的两个operator可能有三种位置组合
#第一种类似9 3 +，即两个operands直接就在operator的前面
#第二种是9 3 + -11 *, 这里对于*而言它的operand是（9+3）和-11，这种形式的特点是单独的那个
#operand A是在由之前的运算得出来的operand B的后面
#第三种是6 9 3 + -11 * /，里的/，对于它而言它的两个operands是[(9+3)*(-11)]的结果和6
#但是这一种的特点是单独的那个operand A是在由之前的运算得出来的operand B的前面

#因此这样一来不能用只把之前的运算结果存到一个variable里，只往stack里push新遇到的单独的数
#的方法，因为这样没办法确定另一个operand到底是在运算的结果的这个operand的前面还是后面
#对于-和/这样的operator而言两个operators的相对位置是matter的

#所以我们必须把运算结果的出的数也push到stack里，这样其实相当于所有的位置组合都是第一种
#即只要碰到了一个operand就从stack里pop出两个作为operators，但是要注意的是
#假设input的意思是op1-op2,那么先pop出来的应该是op2，后pop出来的是op1

#这道题里我们要学到的是，用stack解决的问题，中间得出的结果能push到stack里也要push到stack里
#这样做往往能让整个做题的思路更清晰，不用考虑像这道题这样的第二种和第三种位置组合的情况
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens or len(tokens)==0:
            return None
        else:
            stack=[]
            operands=['+','-','*','/']
            for char in tokens:
                if char not in operands:
                    stack.append(int(char))
                else:
                    #先pop出来的应该是op2，后pop出来的是op1
                    op2=stack.pop()
                    op1=stack.pop()
                    if char == '+':
                        stack.append(op1+op2)
                    elif char=='-':
                        stack.append(op1-op2)
                    elif char=='/':
                        #这里不能用stack.append(op1//op2)
                        #因为在遇到比如6/（-132）的时候6//（-132）的结果是-1
                        #但是按照这道题的要求结果应该是0才可以，所以要用int(op1/op2)
                        #int() work的方式是直接去掉小数部分对于负数也是一样int(-0.1)=0
                        #但是//work的方式是return比/的结果小的那个整数，-1//5=-1
                        stack.append(int(op1/op2))
                    else:
                        stack.append(op1*op2)
            return stack.pop()