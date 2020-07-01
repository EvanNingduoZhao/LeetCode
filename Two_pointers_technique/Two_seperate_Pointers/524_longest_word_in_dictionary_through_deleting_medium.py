class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        # 这是一个用two pointer的helper function，用来看一个string sub是不是另一个string s的substring
        # 这里A是B的sub-string代表B可以在不改变自己内部char的顺序的前提下，只靠delete自己的chars可以得到A。
        def __is_substring(sub, s):
            i = 0
            j = 0
            while i < len(sub) and j < len(s):
                #如果目前的s里的j等于sub里的i的话，那说明我们又在s里找到了sub里的一个元素
                #开始继续在s里往后找有没有sub里的下一个元素，所以i+=1
                if s[j] == sub[i]:
                    i += 1
                #每次不管现在s里的j是不是等于sub里的i
                #这个j看过了，是与不是都要再看s里的一个j了，所以j+=1
                j += 1
            #如果最后while loop走完，发现sub里的最后一个i也在s里找到了，那就return True
            if i == len(sub):
                return True
            #否则return false
            else:
                return False

        # 先cover edge case，如果s或者d有一个是空的那就return空的string
        if not d or not s:
            return ""

        else:
            longest = ""
            #挨个看d里的每一个string
            for string in d:
                #如果这个string比目前找到的longest还要短的话，那就算它是s的substring也没用
                if len(string) < len(longest):
                    continue
                #如果目前的string跟longest的length一样的话
                elif len(string) == len(longest):
                    #如果string的lexicographical order上比longest靠后的话也不行
                    #越大lexicographical order越靠后
                    if string > longest:
                        continue
                    #如果string的lexicographical order比longest靠前的话
                    #且string也是s的substring，把longest更新为等于stirng
                    else:
                        if __is_substring(string, s):
                            longest = string
                #如果string比longest还长，且也是s的substring，也把longest更新为等于stirng
                else:
                    if __is_substring(string, s):
                        longest = string
            return longest