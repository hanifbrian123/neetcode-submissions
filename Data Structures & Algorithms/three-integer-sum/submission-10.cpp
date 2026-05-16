class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());
        // this->printVector(nums);
        for (int i = 0; i < nums.size(); i++)
        {
            int l=0, r=nums.size()-1, target = -nums[i];
            // cout<< "i: "<< i<< " nums[i]: "<< nums[i]<< endl;
            while (l<r)
            {
                // cout<< nums[l]<< ' '<< nums[r]<< " => ";
                if (l==i) {
                    // cout<< "l==i"<< endl;
                    l++;
                } else if (r==i) {
                    // cout<< "r==i"<< endl;
                    r--;
                } else if (nums[l]+nums[r]==target) {
                    // cout<< "= target"<< endl;
                    vector<int> temp = {nums[l], nums[r], nums[i]};
                    sort(temp.begin(), temp.end());
                    res.insert(temp);
                    r--; l++;
                } else if (nums[l]+nums[r]>target) {
                    // cout<< "> target"<< endl;
                    r--;
                } else if (nums[l]+nums[r]<target) {
                    // cout<< "< target"<< endl;
                    l++;
                }
            }
            // cout<< endl<< endl;
            
        }
        vector<vector<int>> ret(res.begin(), res.end());
        return ret;
        
    }
    void printVector(vector<int> &v) {
    for (int & a: v)
    {
        cout<< a<< " ";
    }
    cout<< endl;
}
};