class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for i in strs:
            string += str(len(i))+"#"+i
        return string
    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            ls.append(s[j+1:j+1+length])
            i = j+1+length
        return ls
