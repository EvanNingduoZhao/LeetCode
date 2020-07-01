
# 这里用两头双指针来traverse input String，当两个指针都指向元音字母时，swap这两个字母
# 当有一个指着元音，另外一个没指元音的时候，指的那个pointer停下来等着，等到另外一个也指向元音字母了
# 再swap他俩。

#注意这里的input是string，而string是不可以modified的，所以要新建一个list，再两头指针traverse的过程中
#把不需要swap的直接放到对应位置，需要swap的swap之后再放到对应位置，最后把list转化成string再return

#两头指针的swap的应用的典型还有quick sort和quick select里的partition，详见75题
def reverseVowels2(s):
    vowels = set();
    vowels.update(["a", "e", "i", 'o', "u"])
    i = 0
    j = len(s) - 1
    ans=[None]*len(s)
    while (i <= j):
        if s[i] in vowels and s[j] in vowels:
            ans[i],ans[j]=s[j],s[i]
            i+=1
            j-=1
        else:
            if s[i] not in vowels:
                ans[i]=s[i]
                i+=1
            if s[j] not in vowels:
                ans[j]=s[j]
                j-=1

    return "".join(ans)

print(reverseVowels2("hello"))