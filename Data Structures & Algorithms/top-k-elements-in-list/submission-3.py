class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force method
        """dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i] = 1
        
        return [item[0] for item in sorted(dict1.items(), key=lambda x: x[1], reverse=True)[:k]]"""

        #Bucket Sort
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in dict1.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        