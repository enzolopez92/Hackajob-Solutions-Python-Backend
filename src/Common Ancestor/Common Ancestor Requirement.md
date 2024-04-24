# Common Ancestor Backend Challenge

Find the first (lowest) common ancestor of two nodes in a binary tree without allocating any tree data structure in memory.

The first common ancestor of two nodes v and w is the lowest (i.e. deepest) node that has both v and w as descendants.

Consider the binary tree's indexes starting from 1 in the root, increasing from the leftmost node to the right at each level. (Standard tree node indexing from left to right)

## INPUT

int    index1
int    index2

## OUTPUT

int    indexCommonAncestor

## CONSTRAINTS

1 <= index1 <= 1000000
1 <= index2 <= 1000000

## EXAMPLES

First Case 
### Input
13, 15
### Output
3

Second Case 

### Input
11, 13
### Output
1

Third Case

### Input
10, 11
### Output
5