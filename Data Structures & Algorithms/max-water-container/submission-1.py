class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer1=0
        pointer2=len(heights)-1
        maxarea=0

        while pointer1 < pointer2:
                width=pointer2-pointer1
                height=min(heights[pointer1],heights[pointer2])
                currentarea=width*height
                maxarea=max(maxarea,currentarea)

        
                if heights[pointer1]<heights[pointer2]:
                    pointer1+=1
                else:
                    pointer2-=1
    
        
        return maxarea

