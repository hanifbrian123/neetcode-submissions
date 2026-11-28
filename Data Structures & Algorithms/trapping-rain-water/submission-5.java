class Solution {
    public int trap(int[] height) {
        int[] prefLeft = new int[height.length];
        int[] prefRight = new int[height.length];
        int l = 0, r = height.length - 1, maxL = 0, maxR = 0;
        while (l < height.length) {
            prefLeft[l] = maxL;
            maxL = Math.max(maxL, height[l]);
            l++;
            prefRight[r] = maxR;
            maxR = Math.max(maxR, height[r]);
            r--;
        }
        int res = 0;
        for (int i = 0; i < height.length; i++) {
            res += Math.max(
                Math.min(prefLeft[i], prefRight[i]) - height[i], 0
            );
        }
        return res;
    }
}
