class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        maximum = 0
        counter = 0 
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]] = 1
        for elem in dict:
            if dict[elem]>maximum:
                maximum = dict[elem]
                answer = elem
        return answer    