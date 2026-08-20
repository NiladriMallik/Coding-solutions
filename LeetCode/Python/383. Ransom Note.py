class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {i:0 for i in ransomNote}
        
        for i in ransomNote:
            ransom_dict[i] += 1
        
        for i in magazine:
            if i in ransom_dict.keys():
                ransom_dict[i] -= 1
        
        for i in ransom_dict.values():
            if i > 0:
                return False
        return True

##################################################################

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False

            magazine = magazine.replace(i, "", 1)

        return True