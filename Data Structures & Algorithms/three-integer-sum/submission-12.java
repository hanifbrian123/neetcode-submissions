class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // TWO POINTERS
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        Set<String> set = new HashSet<String>();
        for (int i = 0; i < nums.length; i++) {
            int l = 0, r = nums.length - 1, target = nums[i];
            while (l < r) {
                if (l == i) l++;
                else if (r == i) r--;
                else if (- (nums[l] + nums[r]) == target) {
                    List<Integer> sorted = Arrays.asList(nums[i], nums[l], nums[r]);
                    sorted.sort(Comparator.naturalOrder());
                    String sortedString = sorted.toString();
                    if (!set.contains(sortedString)) {
                        res.add(sorted);
                        set.add(sortedString);
                    }
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



// -1 -1 2 = 0
