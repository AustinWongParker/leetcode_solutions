class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # first attempt

        # nums is array of integers
        # if any value appears at least twice, return true
        # return false is every element is distinct (unique)

        # need a way to iterate thru the nums array
        # 1. for loop ; range of nums
        #    complexitiy: o(n)
        # 2. while loop ; until n-1
        #    comexplity: o(n)
        # 3. sliding window ?? ; two for loops 
        #    complexity:  o(n)
        # 4. hashmap / dictionary ; store keys and check against values
        #   complexity: o(1)

        '''
        temp_dictionary = {}

        for x in range(nums+1):
            if x in temp_dictionary:
                return True
            else:
                # store the value of the iterable (x) in the dictionary as a key
                temp_dictionary[x] = x
        '''

        # ------------------------
        # second attempt - video
        # Notes from neetcode 
        # 1. Can bruteforce, but time complexity will be o(n^2); space: o(1)
        # 2. Sort. It will help see that adjacent values may be the same. Time compexitiy: O(nlogn); space: o(1)
        # 3. HashSet - a hash set is also a collection of objects; A hash set internally uses the hash table data      structure to store data items. Just like a set, a hash set also does not allow storage of duplicate elements.
        #    Q: 'does this value exist in our HashSet'?
        #        Time is O(n) because we only have to go through the values once 
        #    This affects space because we're storing our values if we DO NOT have duplicate values. O(n) for space
        #

        # create variable named hashset that is of type set()
        hashset = set()

        # go through every value of nums array
        for n in nums:
            # is n a duplicate? does it exist in our hashset?
            if n in hashset:
                return True
            # does not contain duplicate? Add it to hashset
            hashset.add(n)
        return False

