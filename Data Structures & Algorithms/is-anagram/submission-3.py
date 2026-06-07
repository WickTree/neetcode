class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ting={}
        for i in s:
            ting[i]=ting.get(i,0) + 1
        for i in t:
            ting[i]=ting.get(i,0) - 1
        return all(j==0 for j in ting.values())
            