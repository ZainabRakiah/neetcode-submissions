class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        n = len(nums)-1
        boundary=0
        jumps=0
        for i in range(n):
            if far==i+nums[i]:
                continue
            if far<=i+nums[i]:
                far = i+nums[i]
            if i == boundary:
                jumps+=1
                boundary = far
            if far>n:
                return jumps
        return jumps

