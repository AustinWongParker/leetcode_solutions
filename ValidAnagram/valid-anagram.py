class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s, hashmap_t = {}, {}

        # Go through each string and add +1 value to value of the hashmap
        for x in range(len(s)):
            hashmap_s[s[x]] = 1 + hashmap_s.get(s[x], 0)
            hashmap_t[t[x]] = 1 + hashmap_t.get(t[x], 0)
        
        # second iteration pass to count each value in the hashmap to see if they're equal
        for character in hashmap_s:
            if hashmap_s[character] != hashmap_t.get(character, 0):
                return False
        
        # if it passes through each for loop, then they must be anagrams!
        return True