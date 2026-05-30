class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Psuedocode:
        #1.Have max counter
        #iterate through list
        #for every 1 in a row update counter
        #once you hit a 0 or end of list:
        #check which is bigger counter or maxcounter
        #update
        #return max counter but make sure max counter is updated 



        maxcounter=0
        counter=0
        for i in nums:
            if i==1:
                counter+=1
            else:
                if counter>maxcounter:
                    maxcounter=counter
                counter=0

        maxcounter=max(counter,maxcounter)
        return maxcounter
