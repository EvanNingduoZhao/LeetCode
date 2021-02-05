# 如果这个code看不懂从下面的视频的8：13开始看
# https://www.youtube.com/watch?v=BXCEFAzhxGY

# 同在code siginal problem这个folder里的prefixSubstring这道题也用了KMP的preprocessing的思想
def preprocessing(pattern):
    M=len(pattern)
    # lps[j]里存的是从pattern[0]到pattern[j]这个substring s里，最长的既是s的prefix也是s的suffix的s的
    # substring的长度
    lps=[0]*M
    i=0
    j=1
    while j<M:
        # pattern[j]永远代表的都是从pattern[0]开始到pattern[j]结束的那个substring的结尾
        # 因此它永远是判定一个prefix是不是一个suffix的焦点
        # 我们还有一点要注意：就是pattern[i]之所以配和pattern[j]进行一次比对，前提是pattern[i]前面
        # 的i个char，都和pattern[j]前面那i个char一一对应，也就是说pattern[:i]这个prefix也是
        # pattern[:j](pattern[:j]不包含pattern[j])的suffix
        # 那么也就是说在这种前提下，如果pattern[j]==pattern[i]，那么pattern[:i+1]这个prefix就是
        # pattern[:j+1]的suffix了，因此如果pattern[j]==pattern[i]，i和j齐头并进，且lps[j-1]=i
        # 至于lps[j-1]=i的细节的index操作问题看notability里的图解
        if pattern[j]==pattern[i]:
            i+=1
            j+=1
            lps[j-1]=i
        else:
            # 如果pattern[j]！=pattern[i]且i！=0，比如说在dsgwadsgz中pattern[3]!=pattern[8]
            # 即w！=z，那么此时我们知道w前面的dsg和z前面的dsg肯定是已经都被我们match上了
            # 那么现在w不等于z，我们要把i的指针从指向w往前退了，那么该退到哪呢？退到w前面的dsg
            # 这个s里最长的既是s的prefix也是s的suffix的s的substring的长度，而对于dsg这个s来说
            # 这个值存在哪呢？答案是lps[i-1]
            if i!=0:
                i=lps[i-1]
            else:
                lps[j]=0
                j+=1
    return lps

# pattern='dsgwadsgz'
# print(preprocessing(pattern))

def KMP_search(text,pattern):
    lps=preprocessing(pattern)
    N=len(text)
    M=len(pattern)
    # i是在text里用的pointer，j是在pattern里用的
    i=0
    j=0
    # res用来存在text中找到的match pattern的substring的结尾的index
    res=[]
    while i< N:
        # 如果match i和j齐头并进
        if text[i]==pattern[j]:
            i+=1
            j+=1
        # 如果齐头并进之后j等于M了说明刚才match上了pattern的最后一个char
        # 那说明找到了一个完整的pattern，那就把它存进res
        if j==M:
            print('found a match')
            res.append(i-1)
            j=lps[j-1]
        # 如果j现在还不等于M，且i也没到text的结尾，且text[i]!=pattern[j]
        # 那么还是那个道理，既然text【i】能和pattern[j]做比对了，那么说明
        # text[i]前面的j个char都完美地match上了pattern[0:j],那么现在发现text[i]!=pattern[j]
        # 要把j这个pointer在pattern中倒退回去多少取决于pattern[0:j]这部分已经在text中match上的substring
        # 里最长的既是suffix也是prefix的substring是多长，那么这个数据存在lps[j-1]里
        # 因此让 j=lps[j-1]
        # 如果j==0，那么没有lps[j-1]，且如果j==0，那说明在text中你还没有match上任何一部分的pattern
        # 那你也没有什么progress可以save，直接increment i吧，看下一个text【i】能不能match上pattern[j]
        elif i<N and text[i]!=pattern[j]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return res
print(KMP_search('aaaab','aaab'))