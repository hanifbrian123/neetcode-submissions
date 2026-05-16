class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        unordered_map<int, unordered_set<int>> mpNumIds;
        unordered_map<string, int> sortedTriplets;
        vector<vector<int>> res;
        for (int i = 0; i < nums.size(); i++)
        {
            mpNumIds[nums[i]].insert(i);
        }
        
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = i+1; j < nums.size(); j++)
            {
                int ijSumMinus = -(nums[i]+nums[j]);
                if (mpNumIds.count(ijSumMinus) > 0) {
                    unordered_set<int> tempSet = mpNumIds[ijSumMinus];
                    tempSet.erase(i);
                    tempSet.erase(j);
                    if (!tempSet.empty()) {
                            vector<int> temp = {nums[i], nums[j], nums[*mpNumIds[ijSumMinus].begin()]};
                            sort(temp.begin(), temp.end());
                            string tempStr = to_string(temp[0]);
                            for (int k = 1; k < temp.size(); k++)
                            {
                                tempStr+=","+to_string(temp[k]);
                            }
                            if (sortedTriplets.count(tempStr)==0) {
                                sortedTriplets[tempStr]++;
                                res.push_back(temp);
                            }
                        }
                }
            }
            
        }
        return res;
        
    }
    void printVector(vector<int> &v) {
    for (int & a: v)
    {
        cout<< a<< " ";
    }
    cout<< endl;
}
};