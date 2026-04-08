class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ordered=sorted(list(set(nums)))
        longest=1
        counter=1
        for i in range(1,len(ordered)):
            if ordered[i]==ordered[i-1]+1:
                counter+=1
            else:
                if longest<counter:
                    longest=counter
                counter=1
        longest=max(longest,counter)
        return longest
                

            
        