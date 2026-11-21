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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        
    }
}
// 1
//     2
//         4, 5
//     3
//         6, 7 
// Pre  : 1 2 4 5 3 6 7
// Ino  : 4 2 5 1 6 3 7
- 4 2 5 [1] 6 3 7
    - 4 [2] 5
        - 4
        - 5
    - 6 [3] 7
        - 6
        - 7

1 2 3 4



// Level: 1 2 3 4 5 6 7