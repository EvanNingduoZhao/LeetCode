#实际上题目里对于string的要求，翻译过来就是
#只要我看到了一个后括号，那么这个后括号就必须和我之前最后见到的那个前括号的对应的
#所以这道题很适合用stack来解
#见到前括号就push进stack里，见到后括号就pop stack，如果pop出来的和见到的这个后括号对应不上
#就return false，能对应上的话就继续

#这道看似很简单的题其实里面还是有不少门道的
#特殊的case有很多 代码实现的时候都要考虑到
#1. 开头就是后括号的
#2. 前括号和string里有的后括号都能对应上，但是前括号的数量比后括号多的
# 等等等
class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True
        else:
            stack = []
            openning = ['(', '[', '{']
            for char in s:
                if char in openning:
                    stack.append(char)
                else:
                    #这个if其实涵盖了很多情况
                    #一一去想这些情况比较难
                    #但是只要养成每次pop一个stack之前都想想，这个stack里是不是一定有东西给我pop
                    #如果没东西给我pop我该怎么办，养成这样的习惯，bug就会少很多
                    if not stack:
                        return False
                    pop = stack.pop()
                    if char == ')':
                        if pop == '[' or pop == '{':
                            return False
                    elif char == ']':
                        if pop == '(' or pop == '{':
                            return False
                    else:
                        if pop == '(' or pop == '[':
                            return False
            # string taverse完，stack也应该空了
            if len(stack) == 0:
                return True
            else:
                return False