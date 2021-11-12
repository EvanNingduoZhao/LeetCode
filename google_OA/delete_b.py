def delete_b(s):
    # dp_left记录从左向左扫，s[:i+1]这个substring里如果要把b删除干净的最小cost（只能从左边的头删或者直接在中间用cost 2删除b）
    # dp_right记录从右向左扫，s[i:]这个substring里如果要把b删除干净的最小cost（只能从右边的头删或者直接在中间用cost 2删除b）
    dp_left = [0]*len(s)
    dp_right = [0]*len(s)
    if s[0]=="b":
        dp_left[0]=1
    if s[-1]=="b":
        dp_right[len(s)-1]=1
    for i in range(1,len(s)):
        if s[i]=="a":
            dp_left[i]=dp_left[i-1]
        else:
            dp_left[i]=min(i+1,dp_left[i-1]+2)
    for i in range(len(s)-2,-1,-1):
        if s[i]=="a":
            dp_right[i]=dp_right[i+1]
        else:
            dp_right[i]=min(dp_right[i+1]+2,len(s)-i)
    # 因为下面的for loop cover不到所以这里res先取全部用dp_left里的或者全部用dp_right里的cost来
    # 删的min
    res = min(dp_left[-1],dp_right[0])
    # 这里就是for loop过一遍 s[:i+1]用dp_left s[i+1:]用dp_right的总cost
    # 如果遇到比当前res更小的总cost就update res
    for i in range(len(s)-1):
        res = min(res,dp_left[i]+dp_right[i+1])
    return res

print(delete_b("abbbaabaabbba"))