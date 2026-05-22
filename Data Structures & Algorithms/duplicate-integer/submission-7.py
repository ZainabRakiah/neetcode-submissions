class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = []
        for i in range(0,len(nums)):
            if nums[i] not in ls:
                ls.append(nums[i])
            else:
                return True
        return False