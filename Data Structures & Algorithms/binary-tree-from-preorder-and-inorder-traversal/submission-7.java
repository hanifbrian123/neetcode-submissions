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
    private int[] preorder;
    private int[] inorder;
    private Map<Integer, Integer> inorderMap = new HashMap<Integer, Integer>(); // inorder value => index
    private int i = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        for (int idx = 0; idx < inorder.length; idx++) { inorderMap.put(inorder[idx], idx); }

        TreeNode root = new TreeNode(preorder[0]);
        int mid = inorderMap.get(root.val);
        if (i + 1 < preorder.length - 1 && 0 <= mid-1) 
            dfs(root, 0, mid - 1, true);
        if (i + 1 < preorder.length - 1 && mid + 1 <= inorder.length - 1)
            dfs(root, mid+1, inorder.length - 1, false);
        return root;
    }

    private void dfs(TreeNode node, int l, int r, boolean isLeftNode) {
        i++;
        TreeNode curNode = new TreeNode(preorder[i]);
        int mid = inorderMap.get(curNode.val);
        // System.out.println(inorder[l] + " " + inorder[r] + " " + mid + " " + isLeftNode + " parent: " + node.val);
        if (isLeftNode)
            node.left = curNode;
        else
            node.right = curNode;
        // System.out.println(
            // "first if: " + (i + 1 < preorder.length - 1 && l <= mid - 1)
            // + " second if: " + (i + 1 < preorder.length - 1 && mid + 1 <= r));
        if (i + 1 < preorder.length && l <= mid - 1)
            dfs(curNode, l, mid - 1, true);
        if (i + 1 < preorder.length && mid + 1 <= r)
            dfs(curNode, mid + 1, r, false);
    }
}

// pre: 1 2 3 4
// ino: 2 1 3 4
// - 2 [1] 3 4
//     - [2]
//         - N/A
//         - N/A
//     - [3] 4
//         - N/A
//         - 4


// 1
//     2
//         4, 5
//     3
//         6, 7 
// Pre  : 1 2 4 5 3 6 7
// Ino  : 4 2 5 1 6 3 7
// - 4 2 5 [1] 6 3 7
//     - 4 [2] 5
//         - 4
//         - 5
//     - 6 [3] 7
//         - 6
//         - 7






// Level: 1 2 3 4 5 6 7