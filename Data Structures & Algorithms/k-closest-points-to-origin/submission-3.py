class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def measure(x1,y1,x2=0,y2=0):
            return math.sqrt((x1-x2)**2 + (y1 - y2)**2)
        
        minHeap = []

        for x,y in points:
            distance = measure(x,y)
            minHeap.append([distance,x,y])
        
        heapq.heapify(minHeap)
        response = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            response.append([x,y])
            k -=1
        return response