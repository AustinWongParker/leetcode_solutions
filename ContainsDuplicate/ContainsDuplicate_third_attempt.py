class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for i in nums:
            if i in mySet:
                return True
            else:
                mySet.add(i) ## had to look up .add during 3rd attempt
        return False
