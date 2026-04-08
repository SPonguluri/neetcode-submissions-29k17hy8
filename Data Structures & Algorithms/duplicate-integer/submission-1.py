class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker=set(nums)
        if len(nums)==len(checker):
            return False
        else:
            return True







        checker=[]
        for i in nums:
            if i in checker:
                return True
            else:
                checker.append(i)
        return False

        