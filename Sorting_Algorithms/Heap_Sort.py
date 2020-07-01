input=[2,8,5,3,9,4,1]



def heap_sort(nums):
    n=len(nums)
    # Build MaxHeap Phase
    # 从n//2-1 开始是因为mid element是第n//2个element 但index是n//2 -1
    for i in range(n//2-1,-1,-1):
        __bubbleDown(nums,n,i)
        #print(nums)

    # Extraction Phase
    #i是用来keep track of heap的last element的index的
    #不用真的traverse到nums的开头，因为如果nums从第二个到最后一个element都在自己正确的位置上了
    #那剩下的第一个element肯定也是在正确的位置上的
    for i in range(n-1,0,-1):
        __swap(nums,0,i)
        #nums[i]是heap的last element，所以heap是nums[:i+1]
        #把新swap到root的原来的last element给bubbledown
        #这个时候nums[i]已经不是heap里的了，所以heap的size是i不是i+1
        #这个heap的size指的是heap里elements的个数
        __bubbleDown(nums,i,0)
        #print(nums)

    return nums


def __swap(heap,i, j):
    # 这是比较python的写法，用来代替temp
    heap[i], heap[j] = heap[j], heap[i]


def __bubbleDown(heap,size,index):
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    # 如果我们要bubble down的这个element有left child，且它的left child还比自己大的话
    # 因为heap是complete，有left child才可能有right child
    # 所以确认要bubble down的element有没有left child，如果有和自己的left child比
    # 这个heap的size指的是heap里elements的个数
    if size-1  >= left and heap[largest] < heap[left]:
        largest = left
    # 如果要bubble down的element比自己的left child小的话，现在这里的largest已经是left了，
    # 所以如果right比left大的话，就把largest变成right
    # 也可能要bubble down的element没有自己的left child大，那么就和自己的right child再比比
    if size-1 >= right and heap[largest] < heap[right]:
        largest = right
    if largest != index:
        # swap 存在index这个index里的我们要bubble down的element和存在largest这个index里的
        # 那个element
        #print('before swap',heap)
        __swap(heap,index, largest)
        #print('after swap',heap)
        # swap之后我们要bubbleDown的element就被存在largest这个index里了，继续recursively
        # 地把它bubbleDown
        __bubbleDown(heap,size,largest)

if __name__ == "__main__":
    print(input)
    print(heap_sort(input))