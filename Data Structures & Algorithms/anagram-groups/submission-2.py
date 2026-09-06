class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        
        def hash(i):
            alphabets = [0]*27
            for j in i: alphabets[ord(j)-ord('a')] += 1
            return tuple(alphabets)
       
        for i in strs:
            l[hash(i)].append(i)
        return list(l.values())
