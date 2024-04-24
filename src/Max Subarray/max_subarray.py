class Solution:
    def run(self, a):
        max_ending_here = max_so_far = a[0]
        
        for num in a[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
