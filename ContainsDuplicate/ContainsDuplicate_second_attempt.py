class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # second attempt
        # solved in ~15-20mins
        # Incorrect - fails on some testcases

        # store our values in a hashmap - { 1 : 2 }
        # For example 1
        #                                  ^ the value 1, shows up twice
        my_dictionary = {}

        # iterate
        for i in nums:
            # if i is in the dictionary, return False immediately
            if my_dictionary.get(i):
                return True
            else:
                # add the value into the dictionary
                my_dictionary[i] = nums[i-1]
        
        # if this return is reached, we know the int array nums has no duplicate values
        return False 

        # if every element is distinct (every value is unique)
        #return False

        # if any value appears at least twice
        #return True
        
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        # have to use set - easiest
        my_set = set()

        # iterate
        for i in nums:
            # if i is in the set, return True immediately
            if i in my_set:
                return True
            else:
                my_set.add(i)
        return False



