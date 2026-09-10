class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        cur=0
        n = len(nums)-1
        for i in range(len(nums)):
            cur = i+nums[i]
            maxi=max(maxi,cur)
            if cur>=n:
                return True
            elif i == maxi:
                return False