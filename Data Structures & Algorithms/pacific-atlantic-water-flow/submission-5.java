class Solution {
    private static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private int n;
    private int m;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        n = heights.length;
        m = heights[0].length;

        boolean[][] pac = new boolean[n][m];
        boolean[][] atl = new boolean[n][m];

        for (int j = 0; j < m; j++) {
            dfs(0, j, pac, heights);
            dfs(n-1, j, atl, heights);
        }

        for (int i = 0; i < n; i++) {
            dfs(i, 0, pac, heights);
            dfs(i, m-1, atl, heights);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (pac[i][j] && atl[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }

        return res;


    }

    public void dfs(int r, int c, boolean[][] visited, int[][] heights) {
        visited[r][c] = true;
        for (int[] d: DIRECTIONS) {
            int nr = r+d[0];
            int nc = c+d[1];
            if (
                nr < 0 || nc < 0 || nr >= heights.length || nc >= heights[0].length 
                || visited[nr][nc] || heights[nr][nc] < heights[r][c]
            ) {
                continue;
            }
            dfs(nr, nc, visited, heights);
        }
    }
}
