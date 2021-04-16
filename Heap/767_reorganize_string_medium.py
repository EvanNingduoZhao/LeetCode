import heapq
# 这道题要想明白一个问题，假设我们的input里有5个a，4个b和2个c，我们得优先把剩余数量最多的字母
# 往我们要返回的res里放，我们不能说先交替放a和c那么最后的结果就会是acacabababb,这样我们在前期没有
# 有效地消耗b，导致最后剩下俩个b连在一起了，这样不行。但是如果我们最开始就交替放a和b的话，结果就是
# abababcabc，这就可以（我们连续加进去三组ab以后变成了剩下2个a,1个b和2个c，这时按照原则我们应该加c进去了）
# 。总结起来我们要用的策略就是每次都往res里加一个目前还剩下的最多的那个，但是不能连着两次都加同一个字母进去
# 那么我们就应该用一个maxHeap来keep track of每个时刻剩下数量最多的字母是什么。
# 具体怎么实现不能连续两次都加同一个字母到res里去，请看27行开始的comment
class Solution:
    def reorganizeString(self, S: str) -> str:
        # 先数出来每个字母有多少个
        count={}
        for char in S:
            if char not in count:
                count[char]=1
            else:
                count[char]+=1
        # 以每个字母的count的相反数作为key放到heap里，之所以用相反数是因为heapq默认是
        # 一个minHeap，想要搞一个maxHeap就得把count的相反数作为key
        maxHeap=[]
        for key, value in count.items():
            maxHeap.append((-value,key))
        heapq.heapify(maxHeap)
        prev_count=0
        prev_char=''
        res=[]
        # 这里为了实现不能连着两次往res里放同一个字母，我们每次把字母和它目前剩下的数量pop出来，
        # 把这个字母加到res里，之后不能直接把剩余count-1和这个字母（code里实际是剩余count+1，因为
        # 在heap里的是count的相反数）push会heap，这样如果剩余count-1在heap里还是最大的话，那么下次
        # heap还会pop出来它，就会导致连续两次往heap里加同一个字母了。因为我们把剩余count-1和这个字母
        # 先存到prev_count和prev_char里，等到下一轮heap pop出来一个新的以后，我们在把
        # prev_count和prev_char push回heap里，因为刚才上一轮已经pop出来过一个不一样的字母了，
        # 之后的这一轮就可以在pop出来prev_char这个字母了。
        while maxHeap:
            negCount,char=heapq.heappop(maxHeap)
            res.append(char)
            # 这个if实际上cover了两种情况：
            # 1是在heap第一次往外pop过后，之前还没有prev_char和prev_count呢，prev_count等于
            # 初始值0
            # 2是当上次pop出来的那个字母的count是1，把这个字母加到res里去1个以后剩余count变成0了
            # 这种情况也不能再push回去了
            if prev_count!=0:
                heapq.heappush(maxHeap,(prev_count,prev_char))
            prev_count=negCount+1
            prev_char=char
        # 最后把res join成一个string，如果这个string和input的长度一样，说明可以通过reorgnize来
        # 得到没有consecutive char的新string
        # 但是如果长度小于input的话，说明最后剩下了多个同一个字母，return ""
        # 假设最后heap里剩下1个a和5个b，先pop出去一个a，那么heap里剩下5个b
        # 之后pop出去一个b，这时我们想要a的count变成0了，不能再被push回heap了
        # 而b也已经被pop出去了，得下一轮才能被push回来，但是因为目前heap空了，不会有下一轮了
        # 因此就导致while loop结束，且res的长度小于input
        res=''.join(res)
        if len(res)!=len(S):
            return ''
        else:
            return res