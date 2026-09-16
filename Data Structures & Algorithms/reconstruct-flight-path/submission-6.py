class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]
        
        '''
        my solution: 
        tickets.sort()
        flight_map = collections.defaultdict(list)
        for src, dst in tickets:
            flight_map[src].append(dst)
        
        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in flight_map:
                return False    

            temp = list(flight_map[src])
            for i, v in enumerate(temp):
                flight_map[src].pop(i)
                res.append(v)
                if dfs(v): return True
                flight_map[src].insert(i, v)
                res.pop()
            return False


        dfs('JFK')
        return res
        '''