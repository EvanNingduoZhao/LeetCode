class Solution:
    #这个问题实际上相当于第278题的一个升级版，
    # 找到range的starting position其实就相当于278题里找第一个bad version
    # (对应下面code里的__searchStart这个helper function)
    #而找range里的ending position则相当于用278题的方法找最后一个good version
    # （对应下面code里的__searchEnd这个helper function）。
    # 当然这两道题还是有一定区别的：
    # 278题的nputlist里的内容只能是good或者bad，碰到mid一个要判定也只有两种情况即mid是good或者mid是bad。
    # 但是这道题的input是数字，那么判定mid时就有三种情况了，即mid<target,mid=target和mid>target.

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        #用来找starting position的helper function
        def __searchStart(nums, target):
            start = 0
            end = len(nums)-1
            while start < end:
                mid = start + (end - start) // 2
                #如果mid小于target，那么target 的range的starting position一定在mid右边
                #mid自己的嫌疑排除了，因此start=mid+1
                if nums[mid] < target:
                    start = mid + 1
                # 如果mid大于target，那么target 的range的starting position一定在mid左边
                # mid自己的嫌疑排除了，因此end=mid-1
                elif nums[mid] > target:
                    end = mid - 1
                # 如果mid自己就等于target，那么mid自己有可能是range的starting position，也有可能
                # starting position其实在mid左侧就已经出现了，因此mid自己还是又嫌疑的，不能排除
                # 这里一定要end=mid，因为starting position是只有可能在左侧，要是让start=mid，那就把
                # 向左找的路堵死了
                else:
                    end = mid
                # 从这里可以看到其实input是good bad这种boolean value和input是数字的区别就在于
                # 如果mid是good，那么就和nums[mid]<target这种情况一样，第一个bad一定在mid右侧
                # 如果mid是bad，那么就和上面的nums[mid]==target的情况一样
                # 而nums[mid]>target在good和bad里是没有对应的
            #因为题中不保证input里是一定有target的，所以我们要进行post processing来check最后start和end重合
            #时指向的到底是不是target的starting position

            #如果inputlist里所有的element全都是大于target的话，最后start和end会在end的初始位置，即len(nums)-1
            #处重合。而如果inputlist里的所有element都是小于target的话，那么start会一直不动，最后end到start的初始
            # 位置来和start重合。这两种inputlist里没有target的情况也可以让while loop达成termination的条件，即
            # start和end重合，因此在return start前，我们要check一下nums[start]到底等不等于target,如果等于才
            # return start，不等于的话就说明是发生了以上两种情况的一种，说明inputlist里没有target，return -1
            if nums[start] == target:
                return start
            else:
                return -1

        #这是用来找target在inputlist里的ending position的。
        #这个helper function比找starting position的helper多了两个parameter，即start和end
        #这是因为在我们找到了target在inputlist里的starting position以后，ending position一定是在starting
        # position右边的，所以在这个helper function里我们的start不需要从0开始了，从上一个helper function
        # 找到的starting position开始就好了
        def __searchEnd(nums, target, start, end):
            while start < end:
                mid = start + (end - start) // 2
                #因为我们start就是从nums里的第一个target开始
                #我们最初的range就是从第一个target到nums的结尾
                #在找Endposition时我们没有机会碰到比target小的值，因此没有必要cover nums[mid]<target
                if nums[mid] > target:
                    end = mid - 1
                else:
                    # 这里要注意，因为我们要找的是ending position，那如果mid是等于target的话，
                    # ending position一定是就是mid或者在mid右侧，因为我们让start=mid
                    start = mid
                    #但是start等于mid有个问题，即在end-start=1时，mid是等于start的，
                    #但我们在mid等于target时还再让start=mid，这样就stuck了
                    #因此我们要在start=end-1时看一下end是不是等于target，如果是的话，那end就是要找的
                    #ending point了，end不等于target的话，start就是要找的ending point
                    if start == end - 1:
                        if nums[end] == target:
                            return end
                        else:
                            return start
            return start

        if not nums:
            return [-1, -1]
        else:
            #先用第一个helper function找 starting point
            left = __searchStart(nums, target)
            #如果starting point是-1的话（即inputlist里没有target），那就没必要再去找ending position了
            #肯定也没有的，直接return [-1,-1]
            if left == -1:
                return [-1, -1]
            #再找ending position时注意要把之前找到的starting position作为start pass 到这个helper function里
            # end还应该是list的结尾处
            right = __searchEnd(nums, target, left, len(nums) - 1)
            return [left, right]
