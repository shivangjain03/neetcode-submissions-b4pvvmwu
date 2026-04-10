class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            if nums[i] == nums[i-1] and i>0:
                continue
            while start<end:
                if nums[i]+nums[start]+nums[end] == 0:
                    output.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                    end-=1
                elif nums[i]+nums[start]+nums[end] < 0:
                    start+=1
                else:
                    end-=1
        return output



        
        