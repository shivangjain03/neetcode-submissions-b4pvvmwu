class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force method
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i] = 1
        
        return [item[0] for item in sorted(dict1.items(), key=lambda x: x[1], reverse=True)[:k]]

        