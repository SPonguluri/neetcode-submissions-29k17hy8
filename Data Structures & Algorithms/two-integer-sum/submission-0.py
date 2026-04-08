class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #here we want to see what indicies of a list add up to the target value
        #so we first want to have a pointer at the zeroth place in the list and one
        #in the 1st place so through those combinations and then if nothing found move
        #the pointer from zeroth place to 1, return pointer indicies in list when a 
        #suitable combination adding up to target is found

        l2=1
        for i in range(len(nums)):
            for l2 in range(len(nums)-1):
                if nums[i]+nums[l2] == target and i!=l2:
                    return [min(i,l2),max(i,l2)]