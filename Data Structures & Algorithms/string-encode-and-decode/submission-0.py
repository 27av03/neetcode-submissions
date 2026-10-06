class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '😂'
        encodedString = '😍'.join(strs)
        return encodedString
    def decode(self, s: str) -> List[str]:
        if s == '😂':
            return []
        if s == '':
            return ['']
        
        return s.split('😍')