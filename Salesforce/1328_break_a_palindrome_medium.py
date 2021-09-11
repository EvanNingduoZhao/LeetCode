# 一个palindrome有三种情况：
# 1.长度只为1，就一个字母，那么你这一个字母你改成什么都还是palindrome所以return ""
# 2.长度为odd，必须abcdzdcba,那么这个string其实是三部分组成的abcd，dcba和中间的z
# 对于这种情况你改中间的z没用，只能改其余的字母才会变成非palindrome
# 3。长度为even，即abcddcba，那么这种情况改哪个都行
# 那么现在讨论怎么能改成lexicographically smallest，
# 想要最小就要把能改成a的字母里最左边的改成a，如果所有能改的字母本身就都已经是a了的话
# 那就把最后一个字母改成b
# 最后一点优化就是实际上我们不需要整个stirng都看一遍，只看前一半就够了，因为后一半和前一半的字母组成是一样的
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        # 1.长度只为1，就一个字母，那么你这一个字母你改成什么都还是palindrome所以return ""
        if length==1:
            return ""
        # 只看前一半，如果长度是odd比如7，那么要看前三个字母即看index是0，1和2的
        # 7//2=3 也合适
        for i in range(0,length//2):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b'