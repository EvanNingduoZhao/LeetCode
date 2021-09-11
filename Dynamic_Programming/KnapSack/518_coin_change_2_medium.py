#这道题的特点是coins这个list里的每一个面额都可以用无限次，但是相同的combination的不同permutation只算一种，即1 2 1和1 1 2只算一种
# （要把这道题的条件和377题的条件区分开，377是相同combination的每一种permutation都算一种）
# 我们这里先讲这道题和494题这种nums里的每个数字只能用一次的且每个cell里也是装方法数的题目类型的区别：
# （这里我们不考虑494题那些正负的复杂layer）
# 对于494这种题目，如果我们选择不放i进去，那么对应的方法数是dp[i-1][j],如果放i进去的话，对应的则是dp[i-1][j-i的value]
# 之所以放i进去是对应的是dp[i-1][j-i的value]就是因为每个数字只能用一次，如果像这道题一样，每个数字可以使用无限次，那么
# 想要（再）放一个i进去时，对应的则是dp[i][j-i的value]。和494题相同的是，当我们选择不放i进去是，对应的都是dp[i-1][j]
# 这里还要注意的就是放i进去时，dp[i][j-i的value-i的value]是不用再加上去一次的，因为在j之前等于（j-i的value）时，我们就考虑过
# dp[i][j-i的value-i的value]了

# 这里再说这道题和377题这种同样都是一个coin或者一个数字可以用无限次，但是一个combination的每一个permutation都算一种的题目类型的区别
# 这道题的解法是对于每个coin的面额，都traverse从0到target amount一轮。这么做的目的是：比如你有2和3的面额，你的target是5，那么在你
# 对于面额2 traverse 0到5时，会发现没有办法组成5。等你对于面额3 traverse 0到5时，你会发现[2,3]这个组合，但是因为你之前已经为面额2
# 做过一次traversal了，所以你永远都不会再碰到【3，2】了。因此保证了一种combination的所有不同permutation都只算一种。

# 现在转回去看377题的notes，那里写了为什么调换内外for loop的循序就使得相同combination的每一种permutation都单独算一种了。

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(0, amount+1)]
        dp[0]=1
        for c in coins:
            for target in range(c, amount+1):
                dp[target]+=dp[target-c]
        return dp[amount]