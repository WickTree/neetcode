class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs=='': return strs
        sizes=[len(i) for i in strs]
        encstr=''.join(j + '#,!!' for j in strs)
        return encstr


    def decode(self, s: str) -> List[str]:
        js=[]
        if s =='': return js
        decoded = s.split("#,!!")
        decoded.pop()
        return decoded

        

