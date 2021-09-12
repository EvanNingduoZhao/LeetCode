# 这道题我们traverse一遍time，如果当前这首歌的时长是20，那么它需要和一首长度为t，where t%60=40的歌来配对成一个pair
# 那么我们只需要一直记录着在目前看到过的song里有多少首歌的时长是t%60=0，1，2，3，4，5。。。59即可
# 因为一共只有0到59这60种可能所以我们用一个length为60的list来做这个记录，freq[i]的值就是目前看到的歌曲时长t%60=i的数量
# 因为对于每首新看到的歌我们都只尝试让它和它左边的歌曲配对，所以不会有重复的
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = [0]*60
        res = 0
        for song in time:
            complement = 60-(song%60)
            # 如果complement=60的话实际上应该是complement=0
            if complement == 60:
                complement = 0
            res += freq[complement]
            freq[song%60]+=1
        return res