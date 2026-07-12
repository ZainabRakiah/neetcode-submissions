class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in  nums:
            dic[i] = 1+dic.get(i,0)
        arr = []
        for cnt, freq in dic.items():
            arr.append([freq,cnt])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
