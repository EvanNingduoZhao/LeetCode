#这道题可以用三个指针，i从nums1最后一个实际有效值开始，k从nums2最后一个值开始，j从nums1最后一个开始
#注意要从尾巴到头遍历
def merge(nums1,m,nums2,n):
    if n==0:
        nums1=nums1
    elif m==0:
        nums1[:]=nums2 # when modifying a input object within a function, 直接写nums1=nums2会让nums1指向一个新的memory slot，要想做到inplace modification需要element wise modify nums1
    else:
        j=m+n-1
        k=n-1
        i=m-1
        while j>=0:
            if nums2[k]>=nums1[i]:
                nums1[j]=nums2[k]
                j-=1
                k-=1
                if k==-1:
                    while i>=0:
                        nums1[j]=nums1[i]
                        j-=1
                        i-=1
            else:
                nums1[j]=nums1[i]
                i-=1
                j-=1
                if i==-1:
                    while k>=0:
                        nums1[j]=nums2[k]
                        k-=1
                        j-=1

nums1 = [0,0,0,0,0]
nums2 = [1,2,3,4,5]

merge(nums1,0,nums2,5)
print(nums1)
