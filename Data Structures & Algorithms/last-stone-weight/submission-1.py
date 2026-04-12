class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
        
        max_heap = [-n for n in stones]  
        heapq.heapify(max_heap)  
        print("Largest element:", -max_heap[0])
        while len(max_heap)>1:
            first_max = -heapq.heappop(max_heap)
            second_max = -heapq.heappop(max_heap)
            print(first_max)
            print(second_max)
            val = first_max-second_max
            if val>0:
                heapq.heappush(max_heap, -val)
        
        if len(max_heap) == 1:
            return -max_heap[0]
        if len(max_heap) == 0:
            return 0
        
        
        