class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Divide into left and right
        # Product = Product of left* Product of right
        output = []
        for i in range(len(nums)):
            prefix = 1
            postfix = 1
            pre_index = i-1
            post_index = i+1

            while pre_index>=0:
                prefix*=nums[pre_index]
                pre_index-=1
            
            while post_index<len(nums):
                postfix*=nums[post_index]
                post_index+=1
            
            output.append(postfix*prefix)
        return output

        