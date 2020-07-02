
class Solution:
    def frequencySort(self, s: str) -> str:
        # 任何sort frequency的题，不管是用count sort，bucket sort还是什么方法
        # 第一步永远是traverse一遍input，记录下来每种item都出现了多少次
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # 在input里一种元素最极端的出现次数要不然就是 input里没有这个字母，即0次
        # 要不然就是全都是这个字母，即len(s)次，因此我们如果想用bucket这个list of lists
        # 的index来store对应位置的list里的item在s里出现的次数的话，那么我们从0到len(s)的index都得有
        # 因此buckets得intialize成len(s)+1个empty list，这里range是0到len(s)+1, 右端点不算
        # 所以0到len(s)一共是len(s)+1个
        buckets = [[] for _ in range(len(s) + 1)]
        # 有把出现了freq次的item放到buckets里的第freq个bucket里
        for key, freq in count.items():
            buckets[freq].append(key)

        #题目要return string，但是因为string是immutable的，所以我们先做一个list
        #再把list和一个empty string joint在一起成为一个string 再return
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i]:
                continue
            else:
                # 可能有好几个字母都在第i个bucket里
                for char in buckets[i]:
                    #如果一个字母char被放在了buckets的第i个bucket里的话，那说明它在s里出现过i次
                    #因此我们append i个char到res里
                    for j in range(0, i):
                        res.append(char)
        return "".join(res)


# 除了用list of lists 来作为buckets以外，还可以用hashtable也就是dict来作为buckets
class Solution:
    def frequencySort(self, s: str) -> str:
        #和上面完全一样
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        #用hashtable做buckets
        buckets = {}
        for key, freq in count.items():
            if freq not in buckets:
                buckets[freq] = [key]
            else:
                buckets[freq].append(key)

        #和上面一个原理
        res = []
        for freq in range(len(s), -1, -1):
            if freq not in buckets:
                continue
            else:
                for char in buckets[freq]:
                    for j in range(0, freq):
                        res.append(char)
        return "".join(res)