class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            sort = tuple(sorted(strs[i]))
            if sort in res:
                res[sort].append(strs[i])
            else:
                res[sort] = [strs[i]]
        return list(res.values())
