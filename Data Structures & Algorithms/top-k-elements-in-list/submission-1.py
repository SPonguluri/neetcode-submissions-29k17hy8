class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #have a dictionary that counts how many times each number appears as we pass through

        #return top k highest appearing numbers

        count={}
        for i in nums:
            count[i]=count.get(i,0)+1

        return heapq.nlargest(k, count.keys(), key=count.get)