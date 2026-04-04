class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # lets create a hashmap(dict) first and push elem there
        # key = int 
        # value = 
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i]=1
        return False

        