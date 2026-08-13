class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i,j]
            elif(i+1==j): #Check if for i=0 all values are checked then increment i to 1,2 and so on
                i+=1
                j=len(nums)-1
            else: #Decrease j for every iteration to compare
                j-=1
        
    
