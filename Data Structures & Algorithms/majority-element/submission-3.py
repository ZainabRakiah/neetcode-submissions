class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        diction = {}
        max_count = 0
        answer = 0
        for i in range(len(nums)):
            if nums[i] in diction:
                diction[nums[i]]+=1
            else:
                diction[nums[i]] = 1
        for elem in diction:
            if diction[elem] > max_count:
                max_count = diction[elem]
                answer = elem
        return answer