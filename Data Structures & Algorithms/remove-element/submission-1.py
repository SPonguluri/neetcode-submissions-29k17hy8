class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                # shift left
                for index in range(i, length - 1):
                    nums[index] = nums[index + 1]
                length -= 1
                # don't increment i
            else:
                i += 1
        return length
        
        
