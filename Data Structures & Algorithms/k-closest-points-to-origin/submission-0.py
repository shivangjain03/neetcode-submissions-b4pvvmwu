class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        import math
        for i in points:
            x = i[0]
            y = i[1]
            temp_dist = math.sqrt((x)**2 + (y)**2)
            dist.append((temp_dist, [x, y]))
        
        heapq.heapify(dist)
        print(dist) 

        result = []
        for i in range(k):
            temp_pop = heapq.heappop(dist)
            result.append(temp_pop[1])
        
        print(dist)
        return result
        


        