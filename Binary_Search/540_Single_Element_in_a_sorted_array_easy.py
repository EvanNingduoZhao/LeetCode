#首先这道题涉及一个很重要的思想，即single element肯定是出现在偶数index的
# （因为前面的pairs都是偶数第一个，奇数第二个（先偶后奇，第一个item在0，第二个在1）
# 这样成为一对，你作为第一个单的，你一定是上一对奇数结尾的那个的下一个，那你一定是偶数index）
# 而且如果出现了一个single element的话，single element是偶数index，那么下一对的第一个
# item就是奇数index，第二个item就是偶数index，这样先偶后奇的pattern就被打破了，
# 从single element往右，所有的pairs都是先奇后偶了。
# 那么我们的思路就是每次得出来一个mid以后，assume它跟它的pairs还是先偶后奇的，如果
# 的确是这样，那就说明single element不在它们左边，在右边。如果不是这样，那就说明
# single element在左边。具体操作如下：
# 我们每次得出来一个mid以后：
# （1）如果这个mid是奇数index，按照assume先偶后奇的原则，应该和它值相等的item
# 应该是是它前面那个偶数index的item。
# （2）相反如果mid是偶数的index，按照assume先偶后奇的原则，应该和它值相等的item
# 应该是是它后面那个奇数index的item。
# 在下面的code里我们管应该和mid是一对的那个item的index叫mid_star

#
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            left=0
            right=len(nums)-1
            # binary search要不就是小于，要不就是小于等于
            #不要写那些left<right-2这种，给自己找麻烦
            while left<right:
                mid=(left+right)//2
                # 如果mid是奇数index，那么mid—star应该是它前面那个
                if mid%2==1:
                    mid_star=mid-1
                    #如果mid和mid——star的值相等的话，那么说明single element在它们右边
                    #那么因为mid是它们这一对中靠右的那一个，因此下一个有嫌疑是single element
                    #的应该是mid+1，因此left=mid+1
                    if nums[mid]==nums[mid_star]:
                        left = mid + 1
                    #相反，如果mid和mid——star的值不相等的话，那么说明single element在它们左边
                    #但这里因为single element只可能是偶数index，而mid是奇数
                    #所以是从包括mid-1这个偶数index在内的向左的所有items有嫌疑，因此right=mid-1
                    else:
                        right = mid-1

                # 如果mid是偶数index，那么mid—star应该是它后面那个
                else:
                    mid_star=mid+1
                    # 如果mid和mid——star的值相等的话，那么说明single element在它们右边
                    # 那么因为mid是它们这一对中靠左的那一个，mid+1和mid是一对的，两者值相等
                    # 所以mid+1是没嫌疑的，mid+2才开始有。这也符合另一个角度，即只有偶数index
                    # 才可以是single element，mid自己是偶数，那么mid+2才是偶数
                    # 因此left=mid+2
                    if nums[mid]==nums[mid_star]:
                        left = mid + 2
                    # 相反，如果mid和mid——star的值不相等的话，那么说明single element在它们左边
                    # mid自己就是偶数，自己就有嫌疑，因此right=mid
                    else:
                        right = mid

            #因为我们每次都把left和right设成single element所在那一侧的第一个可疑的element
            #所以最后while loop结束的时候，是因为left=right了，因此return nums[left]和
            # return nums[right]都是正确的，效果一样
            # 为了证实这个结论可以这样想，single element只能在偶数index上，
            # left和right只会落在可疑的element上，他俩肯定都是同时都是偶数index
            # 因此最后他俩一定会重合不会错开，因为在重合前他俩最近的举例就是left=right-1
            # 它们如果要达到错开，并且还满足两者都是偶数的话，那就得left-right=2
            # 这样需要left里外里增加3（如果原本是right-left=2的话，就是增加4），
            # 但是在right-left=1时，mid=left，而我们最多只有left=mid+2，left值增加了2，不够3
            # 在right-left=2时，mid=left+1，而我们最多只有left=mid+2，left值增加了3，不够4
            # 所以两者永远错不开，因此whileloop最后一定以left==right结尾，因此return谁都可。

            #题干里保证input里一定有single element，因此不需要进行post processing
            return nums[left]