class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #MaxConsecutive Counter=0
        #iterate over nums:
        #if current value[i] ==current Value[i+1]==1:
            #update currentCounter by 1
        #else:
            #compare currentCounter to maxConsective Counter
            #whichever is higher goes into MaxConsecutiveCounter
            #Rest current Counter to 0
        #return Max Consective Counter

        maxConsecutive=0
        currentCounter=0
        for i in range(len(nums)):
            if nums[i]==1:
                currentCounter+=1
            else:
                maxConsecutive=max(maxConsecutive,currentCounter)
                currentCounter=0
        maxConsecutive=max(maxConsecutive,currentCounter)
        return maxConsecutive

