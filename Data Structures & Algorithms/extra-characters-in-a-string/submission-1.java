class Solution {
    Set<String> dictionary;
    int[] dp;
    public int minExtraChar(String s, String[] dictionary) {
        this.dictionary = new HashSet<String>(Arrays.asList(dictionary));
        this.dp = new int[s.length()];
        Arrays.fill(this.dp, -1);
        int res = backtrack(0, new ArrayList<>(), s);
        return res;
    }
    private int backtrack(int idx, List<Integer> cur, String s) {
        if (idx >= s.length()) return 0;
        if (dp[idx] != -1) return dp[idx];

        int minExtra = Integer.MAX_VALUE;
        for (int i = idx; i < s.length(); i++) {
            cur.add(i);
            int l = idx;
            int r = i;
            int extra = getExtra(l, r, s);
            int nextExtra = backtrack(i + 1, cur, s);
            minExtra = Math.min(minExtra, extra + nextExtra);

            cur.remove(cur.size() - 1);
        }
        dp[idx] = minExtra;
        return minExtra;
    }
    private int getExtra(int l, int r, String s) {
        return dictionary.contains(s.substring(l, r+1)) ? 0 : r - l + 1;
    }
}

// "neet","code","neetcode", "desar"

// neetcodesar
// 3 7 10
// 3 5 10

// n * n * n


// ne code neco des
// necodesar



// "neet","code","neetcode"

// neetcodde