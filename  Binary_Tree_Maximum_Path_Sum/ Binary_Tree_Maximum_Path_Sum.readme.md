my first hard problem wish me luck 


A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


This is my first hard leetcode problem... i recently learnt bfs and was inclinde to tackle a BT problem 


We will use recursion for each sub tree and find the max 

Approach:

Define a recursive function that calculates the maximum path sum for each subtree. This function should return two values:

The maximum path sum that includes the current node.
The maximum path sum from the current node upwards (excluding the current node).
In each recursive call, compute the maximum path sum by considering three cases:

The maximum path sum that includes only the current node.
The maximum path sum that includes the left child plus the current node.
The maximum path sum that includes the right child plus the current node.
Keep track of the overall maximum path sum encountered during the recursion.

The result will be the overall maximum path sum.

Psuedo code 

function maxPathSum(root):
    # Initialize a variable to store the overall maximum path sum
    max_path_sum = float('-inf')

    # Define a recursive helper function
    def helper(node):
        nonlocal max_path_sum

        # Base case: If the node is None, return (0, 0)
        if not node:
            return 0

        # Recursive case: Calculate maximum path sums for left and right subtrees
        left_path_sum = max(helper(node.left), 0)
        right_path_sum = max(helper(node.right), 0)

        # Update the overall maximum path sum
        max_path_sum = max(max_path_sum, node.val + left_path_sum + right_path_sum)

        # Return the maximum path sum that includes the current node
        return node.val + max(left_path_sum, right_path_sum)

    # Start the recursion from the root
    helper(root)

    # Return the overall maximum path sum
    return max_path_sum
