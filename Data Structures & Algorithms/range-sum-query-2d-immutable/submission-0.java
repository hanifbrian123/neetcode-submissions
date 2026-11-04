class NumMatrix {
    int[][] pref;
    public NumMatrix(int[][] matrix) {
        int n = matrix.length; 
        int m = matrix[0].length;
        
        this.pref = new int[n+1][m+1];
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < m+1; j++) {
                this.pref[i][j] = (
                    matrix[i-1][j-1] + this.pref[i-1][j] + this.pref[i][j-1] - this.pref[i-1][j-1]
                );
        
            }
            System.out.println(Arrays.toString(this.pref[i]));
        }
        

    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return this.pref[row2+1][col2+1] - (
            this.pref[row1][col2+1] + this.pref[row2+1][col1] - this.pref[row1][col1]
        );
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */