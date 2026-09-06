class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setz = set(nums)
        maxi = 0
        for num in setz:
            if num-1 in setz :
                continue
            start = num
            counter = 1
            while(start+1 in setz):
                counter += 1
                start += 1
            maxi = max(maxi, counter)
        return maxi
