class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #top of our stack
                stackTemp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([temp, i]) # default value is filled in by 0 from res = [0]
        return res


        # Youtube comment
        # A small optimization - you need not store the (key, index) pair. You can just store the index in the queue. For each comparison just reference the array with the index in the queue. Got a faster compute and lesser space.

        # answer = [0] * len(temperatures)
        # stack = []
        # for r in range(len(temperatures)):
        #   while stack and temperatures[stack[-1]] < temperatures[r]:
        #       l = stack.pop()
        #       answer[l] = r-l
        #
        #   stack.append(r)
        #
        # return answer