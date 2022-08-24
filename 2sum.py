class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashMap = {}
        diff = 0
        
        # loop
        for i, element in enumerate(nums):
            # 'math' logic
            # diff = target - element 
            diff = target - element
            
            # if diff is in dictionary, we will return the current i
            # AND the hashmap KEY
            if diff in myHashMap:
                return [i, myHashMap.get(diff)]
            
            # if diff is NOT in dictionary, put current element in hashmap 
            # and keep iterating
            if diff not in myHashMap:
                myHashMap[element] = i
                