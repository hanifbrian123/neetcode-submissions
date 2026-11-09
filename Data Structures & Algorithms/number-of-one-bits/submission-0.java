class Solution {
    public int hammingWeight(int n) {
        int cnt = 0;
        for (double i = 31; i >= 0; i--) {
            double pw = Math.pow(2.0, i);
            if (pw <= n) {
                n -= (int) pw;
                cnt += 1;
            }
        }
        return cnt;
    }
}
