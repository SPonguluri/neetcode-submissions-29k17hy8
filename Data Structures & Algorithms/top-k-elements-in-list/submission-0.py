class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #so here we are given a list of numbers, we need a dictionary 
        #where for each key we keep track of how many times each one appears
        #k is the amount of numbers to return that showed up the most
        dictionary= defaultdict(int)
        for i in nums:
                dictionary[i]+=1

        sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        # extract the top k keys
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result



