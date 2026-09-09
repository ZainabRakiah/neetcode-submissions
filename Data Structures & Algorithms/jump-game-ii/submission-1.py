class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        far = 0
        jumps = 0
        cur_end=0
        for i in range(goal):
            if i == cur_end and far >= goal:
                return jumps+1
            elif far==i+nums[i]:
                continue
            if far<i+nums[i]:
                far = i+nums[i]
            if i == cur_end:
                jumps+=1
                cur_end = far
        return jumps