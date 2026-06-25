class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Traverse nums:
        #if nums[i]==val
        #remove nums[i]
        #shift all values after nums[i] to the left
        while val in nums:
            nums.remove(val)
        return len(nums)

        
        
