class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums[0] < nums[nums.size()-1]) return nums[0];
        int l = 0, r = nums.size()-1;
        while (l<=r)
        {
            int mid = (l+r)/2;
            if (mid!=0 && nums[mid-1] > nums[mid]) return nums[mid];
            else if (nums[mid] < nums[r]) r = mid-1;
            else l = mid + 1;
        }
        return nums[r];
    }
};
