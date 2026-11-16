class Solution {
    int[][] heights;
    int[][] pacCan;
    List<List<Integer>> res = new ArrayList<>();
    int n, m;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        this.n = heights.length;
        this.m = heights[0].length;
        this.pacCan = new int[n][m];
        this.heights = heights;

        // from pacific
        Set<List<Integer>> visitedPac = new HashSet<>();
        for (int j = 0; j < m; j++) {
            dfs(0, j, -1, visitedPac);
        }
        for (int i = 1; i < n; i++) {
            dfs(i, 0, -1, visitedPac);
        }

        // from atl
        Set<List<Integer>> visitedAtl = new HashSet<>();
        for (int j = 0; j < m; j++) {
            dfs(n - 1, j, -1, visitedAtl);
        }
        for (int i = 0; i < n-1; i++) {
            dfs(i, m - 1, -1, visitedAtl);
        }


        return res;

    }

    public void dfs(int r, int c, int heightBef, Set<List<Integer>> visited) {
        if (
            r < 0 || c < 0 || r >= n || c >= m 
            || visited.contains(Arrays.asList(r, c))
            || heightBef > heights[r][c]
        ) {
            return;
        }

        visited.add(Arrays.asList(r, c));
        if (pacCan[r][c] == 1) {
            res.add(Arrays.asList(r, c));
        } else {
            pacCan[r][c] = 1;
        }

        dfs(r, c+1, heights[r][c], visited);
        dfs(r+1, c, heights[r][c], visited);
        dfs(r, c-1, heights[r][c], visited);
        dfs(r-1, c, heights[r][c], visited);
    }
}
