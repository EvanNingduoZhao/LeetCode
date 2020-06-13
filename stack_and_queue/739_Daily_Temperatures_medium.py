#这道题如果用brute force来解的话，那就是以T里的每一个value都为一次起点，向后traverse T，直到发现一个
#值比起点value大的value，算出从起点一共走了多少步，把对于这个起点需要走的步数存到res里，针对每个起点
#都这么做

#但是比如【75，71，69，72，76】，对于以75为起点开始，要找到第一个比75大的76，我们要走过71，69，和72
#但是等待会以71为起点的时候，想找到72，我还得再走一遍69，72。这之中就走了很多重复的路

#如果我们要做的比brute force更好的话，那么我们看过一个T里的element一次，我们就要把它存起来，在T里
#继续往前走，碰到新的element B，只要比存起来的某一个element A大，我们就用B的index减去A的index
#就可以得出以A作为起点的答案了，并且这时A作为起点的答案已经得出了，那就可以把A的信息从存储的信息中
#删掉了

#那么问题是 用什么data structure来存最好呢，答案是stack，碰到的最小的element永远都在
#stack的最后面，只要再碰到一个比最小的稍微大一些的element，立马可以算出以最小的为起点的步数
#把最小的从stack后面pop掉，以后再也不用管了
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #每次往stack里push的是一个tuple
        #tuple的第一项是那一天的温度，第二项是那一天在T里对应的index
        stack=[(T[0],0)]
        res=[None]*len(T)
        #count代表的是现在我们在traverse T的过程中，在T里的位置index
        count=1
        for val in T[1:]:
            while True:
                #如果进行到某一时刻，stack里没东西了，那说明之前看过的所有element我们都
                #已经找到以它们中的每一个为起点对应的步数了，直接把新见到的这个element append到
                #stack上即可
                if len(stack)==0:
                    stack.append((val,count))
                    break
                #如果新见到的这个value比目前stack上最后一个（也应该是最小的）value A大的话
                if val>stack[-1][0]:
                    #算出以A为起点对应的步数
                    res[stack[-1][1]]=count-stack[-1][1]
                    #pop掉A，以后再也不用管了
                    stack.pop()
                # Note：我们现在是在一个while里面，只要新见到的这个value，比stack里的最后一个
                # value大，我们就一直算步数，一直pop，直到stack最后新露出来的这个value的值
                # 大于等于新见到的value位置，我们把新建到的value append到stack里，break出while loop
                else:
                    stack.append((val,count))
                    break
            count+=1
        #T都traverse完了，还没有找到对应步数的天，那对于它们来说就是往后走都没有比它们更暖和的
        #日子了，所以按照题目要求，让res里这些日子为index的值为0
        for i in range(len(res)):
            if not res[i]:
                res[i]=0
        return res

# 以上的那个solution比较容易理解思路
# 以下这个是在上面那个solution的思路的基础上的改进版

#实际上我们可以在stack里只append那一天对应在T的index，因为那一天的温度可以用T[stack[-1]]从T
#里找出来，这里stack[-1] 对应的就是T里的一个index

#下面的这个solution就是把stack里的elements从tuple换成单个的value了
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[0]
        res=[None]*len(T)
        for i in range(1,len(T)):
            while True:
                if len(stack)==0:
                    stack.append(i)
                    break
                if T[i]>T[stack[-1]]:
                    res[stack[-1]]=i-stack[-1]
                    stack.pop()
                else:
                    stack.append(i)
                    break
        for i in range(len(res)):
            if not res[i]:
                res[i]=0
        return res