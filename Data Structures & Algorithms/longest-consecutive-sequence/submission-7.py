class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setz = set(nums)
        ls = []
        for num in setz:
            if num-1 in setz :
                continue
            start = num
            longest = 0
            while(start+1 in setz):
                longest += 1
                start += 1
            ls.append(longest)
        return max(ls)+1
