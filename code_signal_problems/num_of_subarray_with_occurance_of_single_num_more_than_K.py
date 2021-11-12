def getSubarrayCount(nums,k):
    res = 0
    for i in range(len(nums)):
        seen = set()
        for j in range(i,len(nums)):
            if nums[j] not in seen:
                seen.add(nums[j])
                print("seen is:",seen)
                if len(seen)>=k:
                    res+=1
                    print(nums[i:j+1])
    return res



print(getSubarrayCount([1,2,2,4,5,5,8,9],3))

# below method is wrong, don't read
def getSubarrayCount1(nums,k):
    dp = [0]*len(nums)
    dp[0]=1
    seen = set()
    seen.add(nums[0])
    res = 0
    for i in range(1,len(nums)):
        if nums[i] not in seen:
            dp[i] = dp[i-1]+1
            print("dp is:",dp)
            seen.add(nums[i])
            print("seen is:",seen)
            for j in range(1,i+1):
                if dp[i]-dp[j-1] >= k:
                    res+=1
                    print(nums[j:i+1])
            if dp[i] >= k:
                res+=1
                print(nums[:i+1])

        else:
            dp[i]=dp[i-1]
            print("dp is:", dp)
    return res