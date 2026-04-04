class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force method
        # Time comlexity O(n^2) but we need O(n^2)
        # Space complexity = O(n)
        """output = []
        for i in range(len(nums)):
            calc = 1
            for j in range(len(nums)):
                if i!=j:
                    calc*=nums[j]
            output.append(calc)
        return output"""

        # Let's make this solution O(n) rather than O(n^2)
        # Division method
        # Calculate the prod of all non zero number and divide

        zero_count = 0
        mult = 1
        result = []
        for i in nums:
            if i == 0:
                zero_count+=1
            else:
                mult = mult*i

        if zero_count>1:
            return [0]*len(nums)

        if zero_count<1:
            for i in nums:
                result.append(mult//i)
        else:
            for i in nums:
                if i !=0:
                    result.append(0)
                else:
                    result.append(mult)
        return result


        # Prefix Sum
        # Time complexity = O(n)
        
        n = len(nums)
        pref = [0]*len(nums)
        suff = [0]*len(nums)
        result = [0]*len(nums)

        # Initialising the value for suffix and prefix
        pref[0] = 1
        suff[n-1] = 1

        #Populating Prefix
        for i in range(1,n):
            pref[i] = nums[i-1]*pref[i-1]
        
        #Populating suffix
        for i in range(n-2,1,-1):
            suff[i] = suff[i+1]*n[i+1]

        #Populating the result
        for i in rnage(n):
            result[i] = pref[i]*suff[i]
        
        return result 










