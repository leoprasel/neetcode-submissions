class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)
        print(groups)
        for s in strs:
            key = tuple(sorted(s))
            print(key)
            groups[key].append(s)
        result = list(groups.values())
        return result


            