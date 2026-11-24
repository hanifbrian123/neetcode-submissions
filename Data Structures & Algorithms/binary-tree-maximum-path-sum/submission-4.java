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
    public int maxPathSum(TreeNode root) {
        if (root == null) return 0;
        
        int leftV = maxPathSum(root.left);
        int rightV = maxPathSum(root.right);
        return Collections.max(
            Arrays.asList(leftV, rightV, root.val, root.val + leftV + rightV)
        );
    }
}


// each node:
// - only the node => -15
// - just left of the node => -5
// - just right of the node => 40
// - the node + left + right => 25