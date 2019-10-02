# 2D的Dynamic Programming table和center expansion都是palindrom的经典解法
# 两者都是O（n^2）但是center expansion实际上比DP快一些
# center expansion比brute force的O（n^3）好在brute force是每一个potential substring的头尾组合一共n^2种
# check每一头尾组合到底是不是palindrom还需要n 一共就是n^3,
# center expansion 中center一共有2n-1个 围绕每个向两边推进left和right，边推进边检测是不是palindrom，因此只需要O((2n-1)*n)
# 因为蛮力方法的检测方法其实和center expansion的推进方法是类似的，应该想到能够边推进边检查从而节约时间
class Solution(object):
    # This solution utilized DP, I used a 2D table to store previous subproblem results for later use
    # 这个2D table的行和列对应一个substring的start index和end index，table里的entry时true（对应的substring时palindromic）
    # 或者false（对应的substring不是palindromic）
    def longestPalindrome_DP(s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        table = [['False' for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            #DP 的第一个base case即substring长度为1时一定是palindromic
            table[i][i] = 'True'
            result = s[i]
        for i in range(len(s) - 1):
            #DP 的第2个base case即substring长度为2时，只要s[i]和s[i+1]相等就是palindromic
            #只考虑j比i大的情况，因为我们从左往右读，j如果小于i的话就是从右向左读了
            if s[i] == s[i + 1]:
                table[i][i + 1] = 'True'
                result = s[i:i + 2]

        for k in range(2, len(s)):
            for i in range(len(s)):
                j = i + k
                if j < len(s):
                    #本题DP思路中的黄金法则：一个substring是不是palindromic需要满足两个条件：
                    #1.第一个char和最后一个char要一样
                    #2.去掉第一个和最后一个char之后剩下的substring在DP table里要是True
                    if s[i] == s[j] and table[i + 1][j - 1] == 'True':
                        table[i][j] = 'True'
                        result = s[i:j + 1]

        # for row in table:
        #     print(row)

        return result
    def longestPalindrome_Center_Expansion(s: str) -> int:
        max=0
        max_string=''
        n=len(s)
    # 一个长度为n的string可以有2n-1个可以potentially作为palindrom center的位置
    # 可以是每个char上 例如aba的center就是b 也可以是两个char中间 例如aa的center就是a和a中间
    # 这些所有可能的位置加起来一共有2n-1个
        for i in range(2*n-1):
            #对于每个center我们都要给它找到起始左点和起始右点
            #对于a b a这样的string那么b对应的其实是i=2那个center 因为a对应i=0，a和b中间对应i=1，b的实际index也就是2//2=1
            #对于a a这样的string，a和a的中间的center对应的是i=1，它的left应该是a，a的实际index是0=1//2
            left=i//2
            #如果center是在char上那么左右起始点应该是同一个点，因为一个char本身也是一个palindrom，在char上的center的i也都是
            #偶数，所以其对应的i%2为0
            #如果center是在两个char之间的，那么右起始点应该是左起始点+1，在char之间的center对应的i也都是奇数，对应i%2=1
            right=left+i%2
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>max:
                    max=right-left+1
                    max_string=s[left:right+1]
                left-=1
                right+=1

        return max_string

    s="babad"
    c="cbacabd"
    print(longestPalindrome_Center_Expansion(c))