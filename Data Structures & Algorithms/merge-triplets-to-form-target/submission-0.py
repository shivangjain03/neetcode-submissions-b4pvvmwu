class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        out = [1,1,1]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for j in range(len(t)):
                out[j] = max(out[j],t[j])

        if out==target:
            return True
        return False 


        