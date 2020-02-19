def reverseVowels(s):
    vowels = ["a", "e", "i", 'o', "u"]
    i = 0
    j = len(s) - 1
    ans=[None]*len(s)
    while (i <= j):
        if s[i] not in vowels:
            ans[i]=s[i]
            i += 1
        else:
            while (s[j] not in vowels):
                ans[j]=s[j]
                j -= 1
            print("i")
            print(i)
            print("j")
            print(j)
            ans[j] = s[i]
            ans[i] = s[j]
            i += 1
            j -= 1

    return "".join(ans)

def reverseVowels2(s):
    vowels = ["a", "e", "i", 'o', "u"]
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