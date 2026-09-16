class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
    
    #[1,2,3]
    #i=0 , subset = [1], 
        #i=1 , subset = [1,2],
            #i=2 , subset = [1,2,3],
                #i=3 , subset = [1,2,3], res
            #i=2 , subset = [1,2,],
                #i=3 , subset = [1,2,], res
        #i=1 , subset = [1,],
            #i=2 , subset = [1,3],
                #i=3 , subset = [1,3,], res
            #i=2 , subset = [1,],
                #i=3 , subset = [1,], res
    #i=0 , subset = [], 
        #i=1 , subset = [2],
            #i=2 , subset = [2,3],
                #i=3 , subset = [2,3], res
            #i=2 , subset = [2,],
                #i=3 , subset = [2,], res
        #i=1 , subset = [],
            #i=2 , subset = [3],
                #i=3 , subset = [3,], res
            #i=2 , subset = [],
                #i=3 , subset = [], res