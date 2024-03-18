# some of neetcode comments are saying since this is O(n) (instead of O(n*26)), this code is really complex. Could have done with one hashmap

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        
        s1Count = [0] * 26 # [0,0,0,0, ... 0,0]
        s2Count = [0] * 26 # [0,0,0,0, ... 0,0]

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] +=1 #ord function give ASCII value, then subtract lower case a to match the value of the letter
            s2Count[ord(s2[i]) - ord('a')] +=1

        matches = 0
        for i in range(26):
            # this is only case we want to increment our matches
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        # start at len of s1
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            #update matches if not 26
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches +=1 
            # if its too large
            elif s1Count[index] +1 == s2Count[index]:
                matches -= 1

            # opposite cases
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches +=1 
            # if its too large
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


