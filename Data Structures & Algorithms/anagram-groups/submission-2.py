class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = []

        for i in range(len(strs)):
            found = False
            for j in ls:
                if sorted(strs[i]) == sorted(j[0]):
                    j.append(strs[i])
                    found = True
                    break
            if found == False:
                ls.append([strs[i]])
        return ls