class MaxHeap:
    #因为heap是一个complete tree，我们只要知道它有几个elements就知道它长什么样，
    #因此我们用不着用tree来implement它，用list就够了
    #对于一个element A，假设它在list的index是i，那么它的parent的index就是(i-1)//2
    #它的left child的index就是i*2+1，它的right child的index就是i*2+2

    #这里的constructor，我们直接要求input一个nums list，我们直接把它变成一个heap
    def __init__(self,nums=[]):
        self.heap=[]
        for i in nums:
            self.heap.append(i)
            #_floatUp等等internal helper function我们都会在下面实现
            self.__floatUp(len(self.heap)-1)

    # push就是先把new element放到last position 再float up
    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    # peek就是直接return heap的root，也就是list的第一个element
    # 要注意heap是空的情况
    def peek(self):
        if len(self.heap)>=1:
            return self.heap[0]
        else:
            return False

    #pop一个heap需要分类讨论三种情况
    def pop(self):
        #首先在heap里有大于等于1个elements的情况下
        #我们按标准操作来
        if len(self.heap)>1:
            #先把root和last element调换位置
            self.__swap(0,len(self.heap)-1)
            #把刚刚被放到last position的原来的root也就是max pop掉
            max=self.heap.pop()
            #把新放到root位置的原来的last element bubbledown到它该在的位置
            self.__bubbleDown(0)

        #当list里只有一个element的时候当然直接pop掉它自己就好了
        elif len(self.heap)==1:
            max = self.heap.pop()

        #当heap里没东西时，return false
        else:
            max=False
        return max

    def __swap(self,i,j):
        #这是比较python的写法，用来代替temp
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def __floatUp(self,index):
        #先求出要被floatUp的这个new element的parent的index
        parent=(index-1)//2
        #如果这个要被floatUp的element本事就已经是heap的root了，那什么也不用做
        if index==0:
            return
        else:
            #如果这个新的element的确比它的parent大的话
            if self.heap[index]>self.heap[parent]:
                #把它和它的parent swap
                self.__swap(index,parent)
                #继续recursively call这个function
                self.__floatUp(parent)

    def __bubbleDown(self,index):
        left=index*2+1
        right=index*2+2
        largest=index
        #如果我们要bubble down的这个element有left child，且它的left child还比自己大的话
        #因为heap是complete，有left child才可能有right child
        #所以确认要bubble down的element有没有left child，如果有和自己的left child比
        if len(self.heap)-1>=left and self.heap[largest]<self.heap[left]:
            largest=left
        #如果要bubble down的element比自己的left child小的话，现在这里的largest已经是left了，
        #所以如果right比left大的话，就把largest变成right
        #也可能要bubble down的element没有自己的left child大，那么就和自己的right child再比比
        if len(self.heap)-1>=right and self.heap[largest]<self.heap[right]:
            largest=right
        if largest!=index:
            #swap 存在index这个index里的我们要bubble down的element和存在largest这个index里的
            #那个element
            self.__swap(index,largest)
            #swap之后我们要bubbleDown的element就被存在largest这个index里了，继续recursively
            #地把它bubbleDown
            self.__bubbleDown(largest)

if __name__ == "__main__":
    m=MaxHeap([95,3,21])
    m.push(10)
    print(str(m.heap[0:len(m.heap)]))
    print(str(m.pop()))


