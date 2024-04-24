# Implementation Documentation

- We initialize an array lis of length n, where n is the length of the input sequence. lis[i] will store the length of the longest increasing subsequence ending at position i.
- We iterate over each element in the sequence. For each element sequence[i], we compare it with all previous elements sequence[j] (where j < i) to find the longest increasing subsequence that ends with sequence[i].
- If sequence[i] is greater than sequence[j] and the length of the subsequence ending at sequence[j] plus one (lis[j] + 1) is greater than the current length stored at lis[i], we update lis[i] to lis[j] + 1.
After completing this process for all elements, the maximum value in the lis array will represent the length of the longest increasing subsequence in the entire sequence.

### Example:
Let's take the sequence [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] as an example.
At position 0, the longest increasing subsequence is [0] with length 1.
At position 1, the longest increasing subsequence is [0, 8] with length 2.
At position 2, the longest increasing subsequence is [0, 4] with length 2.
And so on...

Finally, the maximum length of the increasing subsequence is 6.

### Complexity Analysis:

The time complexity of this dynamic programming solution is O(n^2), where n is the length of the input sequence.
The space complexity is O(n) for storing the lis array.
Overall, this dynamic programming solution efficiently finds the length of the longest increasing subsequence in the given sequence.