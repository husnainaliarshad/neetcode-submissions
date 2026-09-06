class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = {}
        def hash(i):
            alphabets = [0]*27
            for j in i: alphabets[ord(j)-ord('a')] += 1
            return tuple(alphabets)
        for i in strs:
            if hash(i) not in l:
                l[hash(i)] = [i]
            else:
                l[hash(i)] += [i]
        return list(l.values())
