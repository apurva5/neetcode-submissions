class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        

        heapq.heapify(stones)
        print(stones)

        while len(stones)>1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones,y -x)
            
        return stones[0] * -1 if stones else 0

        
        