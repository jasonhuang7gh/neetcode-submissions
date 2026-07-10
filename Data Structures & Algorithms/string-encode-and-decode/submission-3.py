class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '%'
        else:
            return '-'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '%':
            return []
        else:
            return s.split('-')
