
# 这道题现在的样子是符合标准答案思想的 但是有一些重复判定 不是最精简的，revisit的时候争取写出来精简的
# 主题思路见github page的答案，注意遇到i和j所指的element不相等时，既要考虑把i对应的那个删除后剩下的，也要考虑把j对应的那个删除后剩下的
class Solution:
    #这个method偷懒的方式可以用s==s[::-1]来替代
    #s[::-1] return的是s这个string顺序完全调过来
    def isPalindrom(s,i,j):
        while(i<=j):
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    def validPalindrome(s):
        if len(s)==0 or len(s)==1 or len(s)==2:
            return True
        else:
            removed=False
            i=0
            j=len(s)-1
            while(i<=j):
                if i==j:
                    return True
                elif i+1==j:
                    if s[i]==s[j]:
                        return True
                    else:
                        if removed==False:
                            return True
                        else:
                            return False
                else:
                    if s[j]==s[i]:
                        j-=1
                        i+=1
                    else:
                        if removed==True:
                            return False
                        else:
                            return isPalindrom(s,i+1,j) or isPalindrom(s,i,j-1)


    print(validPalindrome('aba'))