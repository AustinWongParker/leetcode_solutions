class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # neetcode solution

        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

        # time complexity will be ...
        # 0(m * n)
        # m -> number of strings we're given
        # n -> characters in each string