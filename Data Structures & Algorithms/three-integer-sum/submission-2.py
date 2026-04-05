class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force: O(n^3) 
        """nums.sort()
        l = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if i!=j and j!=k and i!=k and nums[i]+nums[j]+nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        l.add(tuple(tmp))
                        
        return [list(i) for i in l]"""

        nums.sort()
        output = set()
        for i in range(len(nums)):
            if i<len(nums):
                    l = i+1
                    r = len(nums)-1

                    while l<r:
                        if nums[i]+nums[l]+nums[r] == 0:
                            tmp = [nums[i], nums[l], nums[r]]
                            output.add(tuple(tmp))
                            l+=1
                            r-=1
                        if nums[i]+nums[l]+nums[r] > 0:
                            r-=1
                        if nums[i]+nums[l]+nums[r] < 0:
                            l+=1
        return [list(i) for i in output]



