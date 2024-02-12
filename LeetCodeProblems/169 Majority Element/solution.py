#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


 class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums2 = sorted(nums,reverse=True)
        high = nums.count(nums[0])
        for i in nums:
            if(i != high):
                if (nums.count(i) > nums.count(high) ):
                    high = i
        return high