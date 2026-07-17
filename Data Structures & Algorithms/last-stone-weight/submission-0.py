import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for num in stones:
            heapq.heappush(heap, -num)
        
        while len(heap) > 1:
            stone1 = -1*heapq.heappop(heap)
            stone2 = -1*heapq.heappop(heap)

            remaining = stone1 - stone2
            if remaining:
                heapq.heappush(heap, -remaining)
            
        if not heap:
            return 0
        else:
            return -1*heapq.heappop(heap)

            