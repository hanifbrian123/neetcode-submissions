/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int res;
    public int maxPathSum(TreeNode root) {
        res = root.val;
        dfs(root);
        return res;
    }
    private int dfs(TreeNode node) {
        if (node == null) return 0;
        int leftVal = node.val + dfs(node.left);
        int rightVal = node.val + dfs(node.right);
        res = Collections.max(
            Arrays.asList(
                res, leftVal + rightVal - node.val, node.val, leftVal, rightVal
            )
        );
        return Collections.max(
            Arrays.asList(
                node.val, rightVal, leftVal
            )
        );
    }
}
// each node:
// - only node
// - left value + right value + node (if left && right)
// - node + left value
// - node + right value
// - left value (if right left)
// - right value (if just right)

// to return:
// - node
// - node + left value
// - node + right value

// each node:
// - only the node => -15
// - just left of the node => -5
// - just right of the node => 40
// - the node + left + right => 25