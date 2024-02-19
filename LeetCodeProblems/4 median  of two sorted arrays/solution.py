class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result = sorted(nums1 + nums2)
        length = (len(result))
        if(length % 2 == 0):
            mid_right = length // 2
            mid_left = mid_right - 1
            return (result[mid_left] + result[mid_right]) / 2.0      
        else:
            return (result[length // 2])