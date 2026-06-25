class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #traverse list
        #at each i have j pointer that goes through and scans the other numberxs and 
        last=len(arr)-1
        for i in range(len(arr)-1):
            maxval=arr[i+1]
            for j in range(i+1,len(arr)):
                    maxval=max(maxval,arr[j])
            arr[i]=maxval
        arr[last]=-1
        return arr



        
        
        
        
        

                