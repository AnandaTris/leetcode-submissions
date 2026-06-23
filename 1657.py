class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counts1 = {}
        counts2 = {}
        for char in word1:
            counts1[char] = counts1.get(char, 0) + 1
        for char in word2:
            counts2[char] = counts2.get(char, 0) + 1
        if set(counts1.keys()) != set(counts2.keys()):
            return False
        return sorted(counts1.values()) == sorted(counts2.values())
