class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1;
        while (l<=r)
        {
            int mid = (l+r)/2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] > target && nums[r] > nums[mid]) r = mid - 1;
            else if (nums[mid] < target && nums[l] < nums[mid]) l = mid + 1;
            else if (nums[mid] > target) {
                if (nums[l] > target) l = mid + 1;
                else r = mid - 1;
            } else {
                if (nums[r] < target) r = mid - 1;
                else l = mid + 1;
            }
        }
        return -1;
    }
};
