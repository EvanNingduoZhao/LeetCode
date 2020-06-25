#Bubble Sort的概念是从头开始traverse，如果一个element比它的下一个element要大的话，就swap他俩
#这样traverse了一遍一后就把list里最大的element放到了list的最右面，那么现在list的最后一个element
#已经是sorted的了。（实际上在第一次traverse中，我们只traverse到list的倒数第二个element，因为
# 见到倒数第二个的时候，把它和最后一个比，这样我们就看过所有的elements了）接下来，我们再从头开始，
# 但这次我们只traverse到倒数第三个，因为最后一个已经sorted的了，我们只需要见到倒数第三个之后拿它的倒数
# 第二个比就好了。以此类推，直到整个list被sort好. 实际上只要在某一次traversal中，没有任何swap发生
# 那就证明这个list已经sort好了。因此我们只要keep 一个boolean flag叫swapped。
# 只有keep了这样的一个boolean flag，在best case的time才是O(n).否则就算上一次traversal中已经没有
# swap发生，list已经sort好了，（假设这是traversal了4次）但是这个algorithm还是会继续对右数第四个
# 左边的list elements继续这个程序。如果是这样的话，那就成了向selection sort那样和input的
# 的顺序无关了。
# bubble sort也是in place的 worst 和 average time complexity是O(n^2) 但是best case的time complexity
# 是O(n).

# 视频教程 很短很好 这里的最后的code inner for loop的loop上限
# 写错了，以自己的code为准 https://www.youtube.com/watch?v=xli_FI7CuzA&t=36s
# 这个视频里的code是没有boolean flag的

input=[2,8,5,3,9,4,1]

def bubble_sort(nums):
    if not nums:
        return None
    #
    swapped=True
    num_of_traversal=0
    while swapped:
        swapped=False
        #用innner loop来traverse
        #i最开始是指向这个list的最后一个，但是因为range是不包含上限的
        #所以第一次只traverse到倒数第二个element
        for j in range(0,len(nums)-1-num_of_traversal):
            #如果目前的这个element比它下一个element大的话就swap它俩
            if nums[j]>nums[j+1]:
                temp=nums[j+1]
                nums[j+1]=nums[j]
                nums[j]=temp
                swapped=True
        num_of_traversal+=1
    return nums

if __name__ == "__main__":
    print(input)
    print(bubble_sort(input))
