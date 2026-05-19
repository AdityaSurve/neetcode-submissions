class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res = res + "25_05" + s
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("25_05")[1:]