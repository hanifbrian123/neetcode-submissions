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
    private int idx = -1;
    private int[] preorder;
    private Map<Integer, Integer> inorderMap = new HashMap<Integer, Integer>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        for (int i = 0; i < inorder.length; i++) inorderMap.put(inorder[i], i);
        return dfs(0, inorder.length - 1);
    }

    private TreeNode dfs(int l, int r) {
        if (l > r) return null;

        TreeNode node = new TreeNode(preorder[++idx]);
        int mid = inorderMap.get(node.val);
        
        node.left = dfs(l, mid - 1);
        node.right = dfs(mid + 1, r);

        return node;
    }
}



// pre: 3 1 2 4
// ino: 1 2 3 4
// 3
//     [1] 2
//         - 
//         - [2]
//     [4]
//         - 
//         - 