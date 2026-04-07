class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Brute force
        dictionary = {}
        for i in nums:
            if i in dictionary:
                return i
            else:
                dictionary[i] = 1
        
        