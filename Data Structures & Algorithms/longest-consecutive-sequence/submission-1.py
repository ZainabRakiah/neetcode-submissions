class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        ls = []
        con_seq = 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                con_seq+=1
            elif nums[i]-nums[i-1]==0:
                continue
            else:
                ls.append(con_seq)
                con_seq = 1
        ls.append(con_seq)
        return max(ls)