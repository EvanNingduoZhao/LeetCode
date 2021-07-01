a=[1,2,3,4,5,6]
b=[7,8,9]

def merge_list(a,b):
    if not a or len(a) == 0:
        return b
    elif not b or len(b) == 0:
        return a
    else:
        i = 0
        res = []
        m = len(a)
        n = len(b)
        while i<min(m,n):
            res.append(a[i])
            res.append(b[i])
            i+=1
        if m<n:
            for j in range(m,n):
                res.append(b[j])
        elif m>n:
            for j in range(n,m):
                res.append(a[j])
        else:
            return res
        return res

print(merge_list(a,b))

