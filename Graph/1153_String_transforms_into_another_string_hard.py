# 下面的答案和讲解参照了这个链接
# https://leetcode.com/problems/string-transforms-into-another-string/discuss/399352/Complete-Logical-Thinking-(This-is-why-only-check-if-str2-has-unused-character)

# 我们可以用一个dict来记录字母和字母之间的mapping关系
# str1里出现过的每一个字母都是一个key，str2里出现过的每一个字母都是一个value
# 一个key value pair就代表一个mapping的关系
# 这道题首先要思考清楚几个原则：
# 1.如果一个字母要被map成大于等于两个字母的话，那一定不行
# 2.如果字母和字母间的mapping存在circle的话，可以用一个在keyset里没出现过的字母作为temp来化解
# 这里仔细讲解以下什么是circle，怎么用temp化解的
# 假设我们要把abc map成bca，那么这里的mapping的关系就是(a:b)(b:c)(c:a),这是一个头尾相连的cicle
# 我们如果不用temp的话是无法解决的，因为如果不用temp的话，就是要先把c变成a 结果是aba，再把b变成c，结果是aca
# 但是当我们想把a变成b时结果就变成了bcb，最开始用c变成的a也被打乱了。想要解决这个问题就只能用一个在str1，即key
# 里没有出现过的letter作为temp。比如我们选择d作为这个temp，那么我们就先把a变成d，结果是dbc，在c变成a，结果是dba
# 再b变成c，结果是dca，最后d变成b，结果是bca，符合我们想要的。
# 那么这里我们可能会以为，既然用temp需要一个在key里没出现过的node，那如果str1里26个字母都用了的话，那就没有没出现
# 过的了，那这种情况下就得return false了吧（这里注意如果key里是26个字母都有，那一定是有cycle的。我们假设英文只有abc
# 三个字母，且abc都在我们的key里。那么如果mapping是a->b->c，c无论指向谁都会有一个cicle，
# 就算a和b都指向c，那还是c指向谁都会有circle，这个情况扩展到26个字母依然valid。）
# 其实不然（不是key里有26个字母就必须是false了），因为如果str2是小于26个字母的话，那就说明
# 有多个key是map到一个value上的，假设a和b都map到c上，那么我们可以先把a变成b，等下再把所有的b都变成c，这样a
# 就空出来了，可以做temp了。但是如果value里，即str2里是26个字母都有的话，那一定是false，首先如果value里是
# 26个字母的话，那么key里一定得也是26个字母，要不然就会有一个key map到多个value上的情况，那也是false。那么如果
# key和value都是26个字母的话，那就说明mapping都是one to one的，不会有多个key map到一个value上的情况，那么
# 我们就没法用上面提到的那个手段来创造temp了，而我们上面也讲了只要key是26个字母都有那就一定有cycle，因此
# 这种情况下一定是false，所以value不能26个字母都有

# 所以想要是true的话只需要遵循两个原则：
# 1.一个key不能map to多个value
# 2是什么且看我下面的总结
# 所以总结下来有cycle没关系，只要有可以用的temp就好，那么当key不是26个字母都有时，那一定有可以用的temp
# 如果key是26个字母都有的话，如果value是少于26个，那就有多个key map to一个value，就可以用上面说的方法创造temp
# 这样也没关系，但是问题就是value是26个的时候是不行的。且在符合第一个条件的前提下key的数量一定是
# 大于等于value的，所以实际上我们不需要care key有多少个，有没有circle这些问题，只要value不是26个，这些问题都可以
# 被解决，但是如果value就是26个的话那就完了。
# 因此第二个条件就是value里不能26个字母都有
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1==str2:
            return True
        trans={}
        for i in range(len(str1)):
            c1=str1[i]
            c2=str2[i]
            if c1 in trans:
                # 这里是监测到一个key map to多个value就立刻return false
                if trans[c1]!=c2:
                    return False
            else:
                trans[c1]=c2
        # 如果上面检测了一圈都没有发现一个key map to多个value的情况
        # 那就检测以下value里是不是只有小于26个不同的字母
        return len(set(str2))<26