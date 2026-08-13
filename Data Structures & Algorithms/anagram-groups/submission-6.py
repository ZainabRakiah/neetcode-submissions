class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            freq = [0] * 26
            for j in i:
                index = ord(j) - ord('a')
                freq[index] += 1
            freq = tuple(freq)
            if freq not in res:
                res[freq] = []
            res[freq].append(i)
        return list(res.values())