class Solution:

    def encode(self, strs: List[str]) -> str:
        #1.we want to iterate through the list
        #2.have a string variable where as we iterate through list
        #we append to the string variable
        #and then return
        encoded=[]
        for i in strs:
            encoded.append(f"{len(i)}#{i}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i, n = 0, len(s)
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            L = int(s[i:j])
            start = j + 1
            end = start + L
            res.append(s[start:end])
            i = end
        return res




            


