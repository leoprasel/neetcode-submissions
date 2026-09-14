class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        '''
        tuples = self.time_map[key]
        for t, v in reversed(tuples):
            if t <= timestamp:
                return v
        return ""
        '''
        tuples = self.time_map[key]
        left = 0
        right = len(tuples) -1
        while left <= right:
            mid = (left + right) //2
            if tuples[mid][0] == timestamp:
                return tuples[mid][1]
            elif tuples[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid -1
        return tuples[right][1] if right >= 0  else  "" 