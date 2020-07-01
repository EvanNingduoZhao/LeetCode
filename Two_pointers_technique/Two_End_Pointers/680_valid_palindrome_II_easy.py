
# 这道题现在的样子是符合标准答案思想的 但是有一些重复判定 不是最精简的，revisit的时候争取写出来精简的
# 主题思路见github page的答案，注意遇到i和j所指的element不相等时，既要考虑把i对应的那个删除后剩下的，
# 也要考虑把j对应的那个删除后剩下的

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 这个helper function用两头指针的办法来check一个string的一部分是不是一个Palindrome
        # 这个helper method偷懒的方式可以用s==s[::-1]来替代
        # s[::-1] return的是s这个string顺序完全调过来
        def is_palindrom(s, i, j):
            while (i <= j):
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        if len(s) <= 2:
            return True
        else:
            i = 0
            j = len(s) - 1
            while (i < j):
                #在两个指针所指的元素的值不相等时
                if s[i] != s[j]:
                    # 分别check 去掉i那个元素以后剩下的从s[i+1]开始到s[j]这部分是不是一个pablindrome
                    # 这里相当于只给删除一个char的机会，因为第一次碰到i和j所指的元素不相等时
                    # 就return下面这个or的结果了，不给你第二次碰到不相等的情况的机会

                    #为什么只check 从i+1到j，或者从i到j-1这部分就够了，因为在中间这一段两侧的部分
                    #肯定是对称的，如果不是的话，肯定之前第一次遇到不对称的地方的时候就走到这一步了
                    return is_palindrom(s, i + 1, j) or is_palindrom(s, i, j - 1)
                #如果碰到的i和j对应的elements一直都是相等的，那就一直这样traverse下去，最后traverse完了
                #就return true
                else:
                    i += 1
                    j -= 1
            return True
