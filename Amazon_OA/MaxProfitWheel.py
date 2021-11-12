def maxProfit(k,profits):
    n = len(profits)
    prev = sum(profits[:k])+sum(profits[n//2:n//2+k])
    print("prev is:",prev)
    mp = prev
    for i in range(1,n//2):
        print(profits[i-1])
        print(profits[(i+k-1)%n])
        print(profits[(i-1+n//2)%n])
        print(profits[(i+n//2+k-1)%n])
        curr = prev-profits[i-1]+profits[(i+k-1)%n]-profits[(i-1+n//2)%n]+profits[(i+n//2+k-1)%n]
        print("new curr is:", curr)
        mp = max(mp,curr)
        prev = curr
    return mp

print(maxProfit(1,[1,5,1,3,7,-3]))