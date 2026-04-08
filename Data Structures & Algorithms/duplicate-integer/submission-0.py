class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #what am I trying to do:
        #so we are given an array and we need to iterate through it. 
        #and keep a list of how many times each number shows up
        #if any number shows up more than once return true, else return false
        #we need some sort of key value pair, key will be numbers and val
        #will be how many times its showed up in the list

        dictionary = {}
        returningBool=False
        for i in nums:
            if i not in dictionary:
                dictionary[i]=1. #dictionary doesnt have a append statement so we need to do it like this
            else:
                dictionary[i]+=1

        for key,value in dictionary.items(): #items allows you to iterate through key and value
            if value > 1:
                returningBool=True
        return returningBool
            

        
        