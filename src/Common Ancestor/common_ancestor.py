class Solution:
    def run(self, index1, index2):
        # Helper function to find the depth of a node
        def depth(index):
            depth = 0
            while index > 1:
                index //= 2
                depth += 1
            return depth
        
        # Helper function to find the parent of a node
        def parent(index):
            return index // 2
        
        # Find the depths of the two nodes
        depth1 = depth(index1)
        depth2 = depth(index2)
        
        # Move the deeper node up to the same depth as the other node
        while depth1 > depth2:
            index1 = parent(index1)
            depth1 -= 1
        while depth2 > depth1:
            index2 = parent(index2)
            depth2 -= 1
        
        # Move both nodes up until they meet at the common ancestor
        while index1 != index2:
            index1 = parent(index1)
            index2 = parent(index2)
        
        index_common_ancestor = index1
        return index_common_ancestor
