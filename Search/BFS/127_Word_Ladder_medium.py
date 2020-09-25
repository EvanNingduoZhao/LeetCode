class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        else:
            # traverse through the wordList to find words that only differ 1 letter from the
            # words in the previous layer of the BFS procedure

            # append them as the next layer in BFS,keep track of their lay index
            # [(word content, layer index)]
            # once we encounter the endword, return current layer index+1
            # if the queue becomes empty before we find the endword, return 0

            # queue里每个元素都是一个tuple，tuple的第一项是每一个word自身，第二项是其在BFS中所处的层数
            queue = [(beginWord, 1)]
            processed = [beginWord]
            while queue:
                currWord, currLayer = queue.pop()
                for word in wordList:
                    #用qualified作为一个flag，如果发现这个word和currWord有多于一个字母不同的话就把它标成False
                    qualified = True
                    #已经被放到过queue里的不再重复考虑
                    if word in processed:
                        continue
                    #mismatch是用来记录word和currWord不一样的字母的数量的
                    mismatch = 0
                    for i in range(0, len(currWord)):
                        if currWord[i] != word[i]:
                            mismatch += 1
                            if mismatch == 2:
                                qualified = False
                                break
                    #如果目前这个word是endWord，且就和currWord只差一个字母，直接return currWord的所在层数+1
                    if word == endWord and qualified == True:
                        return currLayer + 1
                    #如果和currWord只差一个字母但是不等于endWord，那么就把word按照currWord的下一层放到queue里
                    #同时放到processed里记录我们已经把它放到过queue里了
                    if qualified == True:
                        queue.insert(0, (word, currLayer + 1))
                        processed.append(word)
            return 0

#对上面方法做的第一次改进：上面的方法有一个缺点，即在wordlist里找跟某一个currword只差一个字母的单词时，需要把目前
#还没有被放到过queue里的所有单词都过一遍，这样会导致在为不同的currword找与其只差一个字母的单词时，
# 相同的word会被traverse好几次，这样时间效率低
#为了加强时间效率，我们建一个dict叫combo——dict，用来储存符合每一个pattern的word都有什么。pattern的表现方法是这样的，
# h*t就代表开头结尾是h和t且在两者中间有且只有一个字母的单词。我们只需要在这个方法的开头，让每一个wordList里的单词
# 里的每一个字母都当一次这个*，就可以得到这个combo——dict了。得到它的时间复杂度是M^2*N，M是一个word的长度，N是wordList里
#words的数量。每个单词的每个字母都当一次*就一共是M*N次，且在每一次中我们都用了substring的operation，光是用这个operation也
#take M的时间，所以总共是M^2*N。
# 创建combo——dict时每个单词的每个字母都是被access了一次，不会有重复的情况出现，所以效率是比第一种方法要高的
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        else:
            #将每个word的每一个字母都当一次*得到完整的combo_dict
            combo_dict = {}
            for word in wordList:
                for i in range(0, len(word)):
                    expression = word[:i] + '*' + word[i + 1:]
                    if expression in combo_dict:
                        combo_dict[expression].append(word)
                    else:
                        combo_dict[expression] = [word]

            #这里的第二段code和第一种方法的code差不多，区别就是在于是用combo——dict来确定
            #currWord的下一层的word都应该有什么
            queue = [(beginWord, 1)]
            processed = [beginWord]
            while queue:
                currWord, currLayer = queue.pop()
                #让currWord里的每一个字母都作为一次*做出来一个expression
                # 对于每一个expression都到combo——dict里找到符合这个expression的所有words
                #这些words就是所有可以被作为currWord的下一层的words了
                for i in range(0, len(currWord)):
                    expression = currWord[:i] + '*' + currWord[i + 1:]
                    #get的意思是如果dict中有expression就return combo_dict[expression]
                    #如果没有则return []
                    #这里之所以要用get是因为beginWord是不在wordList中的
                    #所以当currWord是beginWord时，有些由currWord生成的expression可能在combo——dict中是没有的
                    for word in combo_dict.get(expression, []):
                        #如果当中有endWord直接return
                        if word == endWord:
                            return currLayer + 1
                        #对于不是endWord，push到queue里，记录到processed的里
                        if word not in processed:
                            processed.append(word)
                            queue.insert(0, (word, currLayer + 1))
            return 0


#对上面方法的再一次改进，再使用combo——dict的基础上再使用bi—directional BFS
#因为随着BFS的层数增多，对于每一层我们需要做的工作是成指数增加的，那么对于一个从起始词变换到目标词一共需要变换6词的题
#我们与其只从起点往终点的方向进行BFS traverse（用一个6层的BFS）不如从起点和终点同时开始用两个各三层的BFS向中间traverse
#让两个BFS在中间汇合，这样总过需要进行的操作数量就少了很多
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        else:
            #构造combo——dict的code还是不变的
            combo_dict = {}
            for word in wordList:
                for i in range(0, len(word)):
                    expression = word[:i] + '*' + word[i + 1:]
                    if expression in combo_dict:
                        combo_dict[expression].append(word)
                    else:
                        combo_dict[expression] = [word]
            #先看下面的code，下面的code中会用到这个helper function
            def _visitWordNode(curr_dir_queue, curr_dir_processed, opp_dir_processed):
                currWord, currLayer = curr_dir_queue.pop()
                for i in range(0, len(currWord)):
                    expression = currWord[:i] + '*' + currWord[i + 1:]
                    for word in combo_dict.get(expression, []):
                        #如果从当前方向的BFS的queue里pop出的currWord的下一层里有一个是
                        #在相对方向的BFS里已经被processed过的word，那说明两个方向汇合了
                        #return 两个方向的层数和
                        if word in opp_dir_processed:
                            # currLayer是word在当前方向的爸爸所处的层数
                            #opp_dir_processed[word]存的是word在相反方向的所处的层数
                            #所以两者的和是没有重复计算的
                            return currLayer + opp_dir_processed[word]
                        if word not in curr_dir_processed:
                            curr_dir_processed[word] = currLayer + 1
                            curr_dir_queue.insert(0, (word, currLayer + 1))
                return None


            #两个方向同时开始的话，两个方向各自需要一个自己的queue
            queue_begin = [(beginWord, 1)]
            queue_end = [(endWord, 1)]
            #两个方向也各自需要一个自己的processed，这里的processed和前面两种方法里的processed有些不同
            #这里的processed是一个dict，key是processed过的word，value是在queue中的层数（相对于起点或者终点）
            processed_begin = {beginWord: 1}
            processed_end = {endWord: 1}
            #两个方向的queue必须都不能为空，有一个空了就说明那个方向的path断掉了，比如起点是hit，终点是cog
            #但是起点往终点的方向只能到hot就断掉了，wordlist中没有hot改一个字母就能变成的了，那么终点到起点的方向
            #也不可能有一个词能改一个字母就变成hot，因为如果有，hot就可以改一个字母变成它了
            while queue_begin and queue_end:
                #_visitWordNode这个helper每次call了以后只从当前方向的queue中pop出一个word来，并做好跟它相关的工作
                # 所以下面的code实际上是从正方向的queue里pop出来一个，从反方向的queue里再pop出来一个，两个方向的BFS是
                #交替进行的
                #且_visitWordNode是在找到了endWord时会return正确的层数和，没找到时return None，所以是只有在
                #if res时才return res
                res = _visitWordNode(queue_begin, processed_begin, processed_end)
                if res:
                    return res
                res = _visitWordNode(queue_end, processed_end, processed_begin)
                if res:
                    return res
            return 0