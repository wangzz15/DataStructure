#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.nums1 = []
        self.nums2 = []
        self.result = 0
        self.len1 = 0
        self.len2 = 0
        self.isEven = True
        self.left_number = 0
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.len1 = len(nums1)
        self.len2 = len(nums2)
        if self.len1 == 0:
            if self.len2 % 2 == 0:
                return (nums2[self.len2 // 2] + nums2[self.len2 // 2 - 1]) / 2
            else:
                return nums2[self.len2 // 2]
        if self.len2 == 0:
            if self.len1 % 2 == 0:
                return (nums1[self.len1 // 2] + nums1[self.len1 // 2 - 1]) / 2
            else:
                return nums1[self.len1 // 2]

        if (self.len1 + self.len2) % 2 != 0:
            self.isEven = False
        self.left_number = (self.len1 + self.len2) // 2 - 1
        left = 0
        right = self.len1 - 1

        Flag = True
        while True:
            p1 = (left + right) // 2
            p2 = self.left_number - p1
            if Flag:
                if p2 < 0:
                    p1 += p2
                    p2 = 0
                if p2 >= self.len2:
                    p1 += p2 + 1 - self.len2
                    p2 = self.len2 - 1
            Flag = False
            if p2 < -1:
                right = p1 - 1
            elif p2 >= self.len2:
                left = p1 + 1

            
            elif p1 < 0 or p2 < 0 or ((p2 + 1 >= self.len2 or nums2[p2 + 1] >= nums1[p1]) and (p1 + 1 >= self.len1 or nums1[p1 + 1] >= nums2[p2])):
                if self.isEven:
                    result = 0
                    if p2 > 0:
                        if p1 < 0:
                            result += nums2[p2 - 1]
                        else:
                            result += max(nums1[p1], nums2[p2 - 1])
                    else:
                        result += nums1[p1]
                    if p1 > 0:
                        if p2 < 0:
                            result += nums1[p1 - 1]
                        else:
                            result += max(nums2[p2], nums1[p1 - 1])
                    else:
                        result += nums2[p2]
                    return result / 2
                else:
                    if p1 < 0:
                        return nums2[p2]
                    elif p2 < 0:
                        return nums1[p1]
                    else:
                        return max(nums1[p1], nums2[p2])
            else:
                if nums1[p1] < nums2[p2]:
                    left = p1 + 1
                else:
                    if left == 0 and right == 0:
                        left= -1
                    right = p1 - 1


        
# @lc code=end
a = Solution()
print(a.findMedianSortedArrays([2,3,4,5,7,8],[1,6]))