class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // TWO POINTERS
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        // System.out.println(Arrays.toString(nums));
        for (int i = 0; i < nums.length; i++) {
            if (i - 1 >= 0 && nums[i - 1] == nums[i]) continue;
            int l = i + 1, r = nums.length - 1, target = -nums[i];
            while (l < r) {
                if (nums[l] + nums[r] == target) {
                    // System.out.println(nums[i] + " " + nums[l] + " " + nums[r]);
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    while (l + 1 < r && nums[l] == nums[l + 1]) { l++; }
                    while (l < r - 1 && nums[r] == nums[r - 1]) { r--; }
                    l++;
                    r--;
                } else if (nums[l] + nums[r] > target) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return res;
    }
}
// -4 -1 -1 0 1 2

// 1 1 1 2 2 3 4 4 5 5
// 1 1 2
// 1

// -1 -1 2 = 0
