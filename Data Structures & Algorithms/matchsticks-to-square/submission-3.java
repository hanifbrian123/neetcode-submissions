class Solution {
    private int[] sides = new int[4];
    private int sum;
    private int[] matchsticks;
    private int sideLength;
    public boolean makesquare(int[] matchsticks) {
        // this.matchsticks = sortReverse(matchsticks);
        this.matchsticks = (matchsticks);
        this.sum = Arrays.stream(matchsticks).sum();
        if (sum % 4 != 0) return false;

        this.sideLength = sum / 4;
        
        return dfs(0);
    }

    private boolean dfs(int idx) {
        if (idx == matchsticks.length) return true;

        boolean res = false;
        for (int i = 0; i < 4; i++) {
            if (sides[i] + matchsticks[idx] <= sideLength) {
                sides[i] += matchsticks[idx];
                res = res || dfs(idx + 1);
                if (res) return res;
                sides[i] -= matchsticks[idx];
            }
        }
        return res;
    }
    private int[] sortReverse(int[] arr) {
        for (int i = 0; i < arr.length; i++)
            arr[i] = -arr[i];
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++)
            arr[i] = -arr[i];
        return arr;
    }
}