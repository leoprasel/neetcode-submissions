class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
            
        from collections import Counter
        left = 0
        right = 0
        t_map = Counter(t)
        missing = len(t)

        res = [(0,0,len(s)+1)]

        while right < len(s):
            if t_map[s[right]] > 0:
                missing -= 1
            if s[right] in t_map:
                t_map[s[right]] -= 1
            
            while missing == 0:
                if right + 1 - left < res[-1][2]:
                    res.append((left, right, right + 1 - left))
                
                if s[left] in t_map:
                    t_map[s[left]] += 1
                if t_map[s[left]] > 0:
                    missing += 1
                left +=1
            right +=1 

        if len(res)>1:
            return s[res[-1][0]:res[-1][1]+1]
        else:
            return ""

            