class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Assumption: len(word1) < len(word2)
        
        final_word = [word1[i] + word2[i] for i in range(min(len(word1), len(word2)))]
        
        if len(word1) < len(word2):
            final_word += word2[len(word1):]
        if len(word1) > len(word2):
            final_word += word1[len(word2):]
        
        return "".join(final_word)