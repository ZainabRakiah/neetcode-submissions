class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i in range(len(nums)):
            if far < i:
                return False
            if far<i+nums[i]:
                far = i+nums[i]
        return True