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
    private int i = 0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        var inToIdx = new HashMap<Integer, Integer>();
        for (int idx = 0; idx < inorder.length; idx++) inToIdx.put(inorder[idx], idx);

        TreeNode root = new TreeNode(preorder[0]);
        i++;
        dfs(root, preorder, inToIdx, root.val);
        return root;
    }
    public void dfs(TreeNode node, int[] preorder, Map<Integer, Integer> inToIdx, int befVal) {
        if (i >= preorder.length) return;
        boolean c = inToIdx.get(preorder[i]) < inToIdx.get(node.val);
        // System.out.println(node.val + " " + preorder[i] + " " + c);

        if (inToIdx.get(preorder[i]) < inToIdx.get(node.val)) {
            node.left = new TreeNode(preorder[i]);
            i++;
            dfs(node.left, preorder, inToIdx, node.val);
            
            if (i >= preorder.length) return;
            node.right = new TreeNode(preorder[i]);
            i++;
            dfs(node.right, preorder, inToIdx, node.val);
        } else if ((inToIdx.get(preorder[i]) > inToIdx.get(befVal)) && (inToIdx.get(node.val) > inToIdx.get(befVal))) {
            // System.out.println("Null Left");
            node.right = new TreeNode(preorder[i]);
            i++;
            dfs(node.right, preorder, inToIdx, node.val);
        } else if ((inToIdx.get(preorder[i]) > inToIdx.get(befVal)) && (inToIdx.get(node.val) < inToIdx.get(befVal))) {
            // System.out.println("Null, Null");
            return;
        } else {
            // System.out.println("Null Left");
            node.right = new TreeNode(preorder[i]);
            i++;
            dfs(node.right, preorder, inToIdx, node.val);
        }
    }
}
