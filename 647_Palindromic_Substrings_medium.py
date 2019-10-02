class Solution:
    # Dynamic Programming method O(n^2)
    def countSubstrings_DP(s: str) -> int:
        count=0
        dp_table=[[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp_table[i][i]=True
            count+=1
        for j in range(len(s)-1):
            if s[j]==s[j+1]:
                dp_table[j][j+1]=True
                count+=1
        for k in range(2,len(s)):
            for m in range(len(s)):
                n=m+k
                if n<len(s):
                    if s[m]==s[n] and dp_table[m+1][n-1]==True:
                        dp_table[m][n]=True
                        count+=1
        # print(dp_table)
        return count

    # Center Expansion Method O(n^2)
    # although same time complexity but center expansion is faster
    # 讲解视频链接：https://www.youtube.com/watch?v=RGes8vSjw9U
    def countSubstrings_Center_Expansion(s: str) -> int:
        count=0
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
                count+=1
                left-=1
                right+=1
        return count



    print(countSubstrings_Center_Expansion('aaa'))