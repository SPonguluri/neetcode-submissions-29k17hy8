class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #right here we have a right and left pointer at the biggest number and smallest number
        l=0
        r=len(numbers)-1
        while numbers[r] + numbers[l]!=target:
            if numbers[r] + numbers[l] > target:
                r+=-1
            elif numbers[r] + numbers[l] < target:
                l+=1
        return [l+1,r+1]

