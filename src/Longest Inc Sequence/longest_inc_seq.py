class Solution:
    def run(self, sequence):
        n = len(sequence)
        # Initialize an array to store the length of longest increasing subsequence ending at each index
        lis = [1] * n
        
        # Iterate over each element in the sequence
        for i in range(1, n):
            # For each element, check all previous elements to find the longest increasing subsequence
            for j in range(i):
                if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        
        # The maximum length of increasing subsequence will be the maximum value in lis array
        max_length = max(lis)
        
        return max_length

