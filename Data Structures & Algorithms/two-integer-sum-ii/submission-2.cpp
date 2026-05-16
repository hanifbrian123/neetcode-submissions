class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0, r=numbers.size()-1;
        while (l<r)
        {
            int twosum = numbers[l]+numbers[r];
            if (twosum == target) {
                return {l+1,r+1};
            } else if (twosum < target) {
                l++;
            } else {
                r--;
            }
        }
        return {};
        
    }
};