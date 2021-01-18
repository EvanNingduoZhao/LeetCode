# 答案直接看这个吧
# https://leetcode.com/problems/string-transforms-into-another-string/discuss/399352/Complete-Logical-Thinking-(This-is-why-only-check-if-str2-has-unused-character)
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1==str2:
            return True
        trans={}
        for i in range(len(str1)):
            c1=str1[i]
            c2=str2[i]
            if c1 in trans:
                if trans[c1]!=c2:
                    return False
            else:
                trans[c1]=c2
        return len(set(str2))<26