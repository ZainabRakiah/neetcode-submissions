class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums)-1
        range_so_far=0
        max_range = 0
        for i in range(len(nums)):
            range_so_far = i+nums[i]
            max_range=max(range_so_far,max_range)
            if max_range>=last_index:
                return True
            elif i == max_range:
                return False
            
