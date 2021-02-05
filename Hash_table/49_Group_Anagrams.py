class Solution:
    # 这是第一种方法，思想是如果两个strings被sort之后的结果是一样的话，那么两者就是anagrams
    # time:O(n*klogk) space:O(nk)
    # n是strs的size，k是最长的string的长度
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            # sorted(s)的结果是个list，list不是hashable的，因此要转换成tuple
            sortedS = tuple(sorted(s))
            if sortedS in res:
                res[sortedS].append(s)
            else:
                res[sortedS] = [s]
        return res.values()

    # 这是第二种更优的方法，这种方法的思想是只要两个string，各自中每个字母出现的频数是一样的，那么两者就是anagrams
    # 过一遍strs里的每一个string，给每一个string都建一个长度为26的list count
    # 其中count[i]里存着在这个string中字母表中的第i个字母出现了多少次
    # 之后把这个list给转化成一个tuple，tuple是hashable的可以作为dict的key
    # time:O(nk) space:O(nk)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            # 从头到尾实际上都只用了一个长度是26的list
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            # 把这个list给转化成一个tuple
            count=tuple(count)
            if count in res:
                res[count].append(s)
            else:
                res[count]=[s]
        # 只要return dict的values就好了，自动就是一个符合要求的list of lists
        return res.values()