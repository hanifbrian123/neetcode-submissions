class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0, r=numbers.size()-1;
        while (l<r)
        {
            int twosum = numbers[l]+numbers[r];
            if (twosum == target) {
                vector<int> ans = {l+1,r+1};
                return ans;
            } else if (twosum < target) {
                l++;
            } else {
                r--;
            }
        }
        vector<int> ans = {-1,-1};
        return ans;
        
    }
};