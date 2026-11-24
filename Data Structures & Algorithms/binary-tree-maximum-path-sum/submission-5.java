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
        int res = root.val;
        if (root.left != null && root.right != null) {
            int leftV = maxPathSum(root.left);
            int rightV = maxPathSum(root.right);
            res = Collections.max(
                Arrays.asList(leftV, rightV, root.val, root.val + leftV + rightV)
            );
        } else if (root.left != null) {
            int value = maxPathSum(root.left);
            res = Collections.max(
                Arrays.asList(value, root.val, root.val + value)
            );
        } else if (root.right != null) {
            int value = maxPathSum(root.right);
            res = Collections.max(
                Arrays.asList(value, root.val, root.val + value)
            );
        }

        return res;
    }
}


// each node:
// - only the node => -15
// - just left of the node => -5
// - just right of the node => 40
// - the node + left + right => 25