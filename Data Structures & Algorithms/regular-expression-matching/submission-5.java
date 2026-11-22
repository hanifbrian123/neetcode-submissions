class Solution {
    private Boolean[][] dp;
    private String s, p;
    public boolean isMatch(String s, String p) {
        int n = s.length(), m = p.length();
        this.s = s; this.p = p;
        dp = new Boolean[n][m];
        return dfs(0, 0);
    }
    private boolean dfs(int i, int j) {
        if (i >= s.length() && j >= p.length()) return true;
        if (i >= s.length() || j >= p.length()) return false;
        if (dp[i][j] != null) return dp[i][j];

        if (j + 1 < p.length() &&  p.charAt(j + 1) == '*') {
            dp[i][j] = (
                dfs(i, j + 2) ||
                (p.charAt(j) == '.' || p.charAt(j) == s.charAt(i)) && dfs(i + 1, j + 2) ||
                (p.charAt(j) == '.' || p.charAt(j) == s.charAt(i)) && dfs(i + 1, j)
            );
        } else if (p.charAt(j) == '.' || p.charAt(j) == s.charAt(i)) {
            dp[i][j] = dfs(i + 1, j + 1);
        } else {
            dp[i][j] = false;
        }
        return dp[i][j];
    }
}

// nnn
// n*



// a a
// . b


// n n n
// n *

// x y z
// y * z
// take 1 + -> take 1 -> take 1

// take 0
// i
// j + 1

// take 1
// i + 1
// j + 1

// take 1 +
// i + 1
// j