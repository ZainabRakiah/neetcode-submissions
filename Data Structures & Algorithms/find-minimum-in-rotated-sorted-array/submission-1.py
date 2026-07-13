class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if nums[l]<nums[r]:
            return nums[l]
        mini = nums[r]
        
        while(l<r):
            mid = l+(r-l)//2
            if nums[mid] < mini:
                mini = nums[mid]
                r = mid
            elif nums[mid]>mini:
                l = mid+1
            else: l+=1
        return mini