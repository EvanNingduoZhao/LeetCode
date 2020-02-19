def findLongestWord(s, d):
    if len(s) == 0 or len(d) == 0:
        return ''
    else:
        firstfound = False
        ans = ''
        for string in d:
            i = 0
            # 用这个方法看一个stirng in d 是不是能靠删s里的characters来得到
            for c in s:
                if i < len(string) and c == string[i]:
                    i += 1
            ## i == len(sting)就代表s里有每一个d里这个string里面的characters
            if i == len(string):
                if firstfound == False:
                    ans = string
                    firstfound= True
                else:
                    if len(string)>len(ans):
                        ans = string
                    elif len(string)==len(ans):
                        if string<ans:
                            ans=string
        return ans

## we can sort the dict by the criteria stated in the question, longer strings gets placed 靠前，长度一样时按lexicographical order

def findLongestWord_with_sorting(s, d):
    if len(s) == 0 or len(d) == 0:
        return ''
    else:
        # here we use a lambda function to sort the dict
        # the lambda function returns a tuple as the sorting key, the first element is negetive length (这样越长越靠前)，the second is string itself (长度一样时按lexicographical order)
        d.sort(key= lambda word: (-len(word),word))
        for string in d:
            i = 0
            for c in s:
                if i < len(string) and c == string[i]:
                    i += 1
            if i == len(string):
                return string
        return ""


s="abpcplea"
d=["ale","apple","monkey","plea"]
print(findLongestWord_with_sorting(s,d))