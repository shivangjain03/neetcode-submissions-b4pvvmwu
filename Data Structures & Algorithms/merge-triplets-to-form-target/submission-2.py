class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [1,1,1]
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            for j in range(3):
                res[j] = max(res[j],i[j])
        print(res)
        return res == target

