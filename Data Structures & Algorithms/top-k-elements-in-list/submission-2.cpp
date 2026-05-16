class Solution {
    public: vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (auto &num: nums) {
        freq[num]++;
    }
    unordered_map<int, vector<int>> freqAsIdx;
    for (auto &pair: freq) {
        freqAsIdx[pair.second].push_back(pair.first);
    }
    
    int cnt = 0, i = nums.size();
    vector<int> ans;
    while (cnt<k)
    {
        if (freqAsIdx.count(i)>0) {
            int j = 0;
            cout<< "====="<< endl;
            cout<< i<< ':'<< endl;
            while (cnt<k && j<freqAsIdx[i].size())
            {
                ans.push_back(freqAsIdx[i][j]);
                cnt++;
                cout<< cnt<< ' '<< j<< ' '<< freqAsIdx[i][j];
                j++;
            }
            cout<< endl<< endl;
        }
        i--;
    }
    cout<< endl<< endl<< endl;
    return ans;

              
    }
};
