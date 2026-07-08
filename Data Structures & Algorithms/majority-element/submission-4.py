class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        max = 0
        answer = 0
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        for j in dict:
            if dict[j]>max:
                max = dict[j]
                answer = j
        return answer