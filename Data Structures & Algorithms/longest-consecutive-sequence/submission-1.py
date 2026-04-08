class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter=1
        maxlength=0
        if len(nums)==0:
            return 0
        nums=sorted(set(nums))
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                counter+=1
            else:
                if counter>maxlength:
                    maxlength=counter
                counter=1
        return max(maxlength,counter)



