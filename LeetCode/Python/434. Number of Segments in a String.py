class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

#################################################################

class Solution:
    def countSegments(self, s: str) -> int:
        segments = []
        segment = ''
        for i in s:
            print(f'Character: _{i}_')
            if i != ' ':
                segment = f"{segment}{i}"
            else:
                if segment:
                    segments.append(segment)
                segment = ''
        if segment:
            segments.append(segment)
        print(segments)
        return len(segments)
        