class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #join arrays -> sort -> get middle value O(n log n)

        #selecting a and b, a being the smallest
        size_nums1 = len(nums1)
        size_nums2 = len(nums2)
        if size_nums1 <= size_nums2:
            a = nums1
            size_a = size_nums1
            b = nums2
            size_b = size_nums2
        else:
            a = nums2
            size_a = size_nums2
            b = nums1
            size_b = size_nums1


        '''
        A = [1,3]
        B = [2,7,8,9,10]
        how many from A? -> i
        how many from B? -> j
        '''
        total = size_a + size_b
        half = total//2

        #for i in range(1,len(a)+1): #o(n)
        left, right = 0, size_a

        def check_i(i,j):
            if i == 0: 
                a_left_max = -float('inf')
            else:
                a_left_max = a[i-1]

            if i >= size_a:
                a_right_min = float('inf')
            else:
                a_right_min = a[i]

            if j==0:
                b_left_max = -float('inf')
            else:
                b_left_max = b[j-1]

            if j >= size_b:
                b_right_min = float('inf')
            else:
                b_right_min = b[j]

            min_boundary = min(a_right_min, b_right_min)
            max_boundary = max(a_left_max, b_left_max)
            
            if a_left_max <= b_right_min:
                if b_left_max <= a_right_min:
                    return True, '', min_boundary, max_boundary
                else:
                    return False, 'increase', min_boundary, max_boundary
            else:
                return False, 'decrease', min_boundary, max_boundary

        while left <= right:
            i = (left + right) //2
            j = half - i
            gate, i_direction, min_boundary, max_boundary = check_i(i,j)
            if gate:
                if total % 2 == 0:
                    res = (min_boundary + max_boundary)/2
                else:
                    res = min_boundary
                return res
            elif i_direction == 'increase':
                left = i + 1
            else:
                right = i -1
        return ""



'''
nums1=[1,3]
nums2=[2,4]
total = 4
half = 2
left = 0 right =2 
i=1 j=1
'''


         