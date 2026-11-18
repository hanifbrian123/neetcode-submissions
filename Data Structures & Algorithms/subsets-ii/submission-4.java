class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        var bucket = new int[41];
        var set = new HashSet<String>();
        dfs(0, cur, subsets, nums, bucket, set);
        return subsets;
    }
    public void dfs(int i, List<Integer> cur, List<List<Integer>> subsets, int[] nums, int[] bucket, Set<String> set) {
        if (i==nums.length) {
            String s = Arrays.toString(bucket);
            if ( ! set.contains(s) ) {
                List<Integer> copy = new ArrayList<>(cur);
                subsets.add(copy);
                set.add(s);
            }
            return;
        }

        cur.add(nums[i]);
        bucket[nums[i]+20]++;
        dfs(i+1, cur, subsets, nums, bucket, set);


        cur.remove(cur.size() - 1);
        bucket[nums[i]+20]--;
        dfs(i+1, cur, subsets, nums, bucket, set);
    }
}
