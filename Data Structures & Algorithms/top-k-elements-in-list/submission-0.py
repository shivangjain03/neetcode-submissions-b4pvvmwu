class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # So lets create a dict1
        # dict1-> key = number in intyeger array nums, value = occurence of that number 
        # then traverse the dict by value 
        # return the first kth keys like 1,....k

        output = []
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i] = 1
        
        sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse = True))

        for i in sorted_dict:
            if k!=0:
                output.append(i)
                k=k-1
        
        return output