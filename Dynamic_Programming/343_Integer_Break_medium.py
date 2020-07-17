#以下是dp解法的solution
#这道题的思路是这样的，首先想的是brute force的方法，
#这里首先要进行一个observation，即把一个大数n分成若干个小的整数其实可以看成先把这个大数n分成两个数a和b，再把a和b
#再分别各自分成两个数。那么有一个问题是，把一个数分成若干个component以后，在每个component小于多少的情况下就不需要再分了
#答案是小于5就不用在分了。因为1分不了，2分成两个1的乘积是1，which小于2自身，因此不合算。3可以分成1和2乘积是2小于3自身，因此
#也不合算，4可以分成1和3或者两个2，但是更大的两个2的乘积也只是等于4自身所以还是没必要。所以只有大于等于5的数才值得被再分一次

# 在最brute force情况下：
# 即假设input是10，那么我们就要算一下把10分成1和9，2和8，3和7，4和6，以及5和5，（这里所有产生的大于等于5的数字都是要再分的）
# 之后把大于等于5的数字再逐步分成小于5的数字，所产生的一组（一共和等于10的）数的总乘积是多少。把这5种初始分法所对应的最终
# 的总乘积相比较，最后return乘积最大的那个。要注意的是，在算1和9这种初始分法时，我们接下来就需要recursively地call
# 这个method去算怎么分9可以得到最大
# 的总乘积，那么分9就涉及到1和8，2和7，3和6，4和5等初始分法。那么比如说这里算了一次5的最优分法的总乘积是多少，但是在之后
# 算8的，7的和6的最优分法的时候还需要再算5的最优分法，这样重复地完成同一个任务使得效率很低。因此第一个我们可以做的优化就是
# 用一个dp array把算过的每个数的最优分法的总乘积存起来，这样在之后再需要算其他数的最优分法时在需要用到这个数的最优分法的总乘积
#时就不要再真的算一遍，只需要在dp array里找就好了。

#但是现在我们这个方法是top down的，我们在memory里还需要存一个recursion stack。但是我们如果用bottom up的方法就不需要
#recursion stack。下面的方法就是buttom up的
#这种题在面试时不要上来就尝试想最优解，先跟面试官说brute force的再一步一步优化
class Solution:
    def integerBreak(self, n: int) -> int:
        #如果input n就是小于5的，那题目要求我们必须分，那就从1到4挨个分类讨论之后return就好了
        if n<5:
            if n==1:
                return 1
            elif n==2:
                return 1
            elif n==3:
                return 2
            else:
                return 4
        #如果n大于等于5
        else:
            #这里我们dp array的第一位是不用的，用一个0在那边做place holder
            #因此dp[i]里存的就是i的最优分法的总乘积
            dp=[0,1,2,3,4]
            #从5到n的所有数字挨个计算最优分法的总乘积
            for i in range(5,n+1):
                maxProduct=0
                #对于每个数，我们计算它的总乘积的方法是，把1和i-1，2和i-2，一直到i//2和i//2（对于偶数i）
                #或i//2和i//2+1（对于奇数i）的这些初始分法对应的最后的总乘积都算出来，之后return最大的那个
                #但是注意 这里对于没一种初始分法的总乘积，我们只需要O(1)时间就可以算出来。因为在我们计算i的
                #最优分法总乘积时，我们以及把1到i-1的最优分法的总乘积都算完且存在dp里了，因此对于1和i-1这种初始分法
                #的总乘积我们直接用dp[1]*dp[i-1]就可以算出来了
                for j in range(1,i//2+1):
                    maxProduct=max(maxProduct,dp[j]*dp[i-j])
                dp.append(maxProduct)
            #当我们把dp这个array填满了以后
            res=0
            #把1和n-1，2和n-2这些初始分法都的总乘积都算出来，最后return最大的那个总乘积
            for i in range(1,n//2+1):
                res=max(res,dp[i]*dp[n-i])
            return res

#以上这种方法的time是O(n^2) space是O(n)
#在以上方法的基础上，再做一个数学上的观察，就可以得出一个time是O(n),space是O(1)的算法
#因为只要是5以上的数就值得继续被拆分，而拆分就可以被拆分成1 2 3 4，首先拆成1肯定是不划算的，因为1不给product做任何贡献
#其次拆成4就等于拆成两个2。因此任何一个数最后的最优拆分法其实都是把这个数拆成若干个2和3，但是关于2和3具体该怎么选择呢
#答案是应该尽量拆成3，那么在n不是3的倍数时我们就要用2，比如如果n/3等于k余1的情况下，那么我们就应该拆成k-1和3和一个4，之后
#把那个4拆成两个2,因为2*2>1*3. 如果n/3=k余2，那就直接是k和3和1个2了
class Solution:
    def integerBreak(self, n: int) -> int:
        if n<5:
            if n==1:
                return 1
            elif n==2:
                return 1
            elif n==3:
                return 2
            else:
                return 4
        else:
            product=1
            #等于4时就意味着再减一个3就要余1了，因此直接product在下面*4相当于乘以2*2，相当于把最后一个4拆成2和2而不是3和1
            #等于3时就是能除尽3
            #等于2时就是k个3和1个2
            #不会等于1
            while n>4:
                n-=3
                product*=3
            product*=n
            return product