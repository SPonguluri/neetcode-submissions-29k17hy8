class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so here we want to keep the original list, but sort all of them into order
        #return the ones that are the same in similar order
        dictionary = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))  # <-- use sorted version of string as key
            dictionary[key].append(s)  # <-- group anagrams together
        return list(dictionary.values())