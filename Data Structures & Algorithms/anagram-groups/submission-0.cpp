class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> res;
        for (auto s: strs) {
            vector<int> cnt(26);
            for (char c: s) {
                cnt[c - 'a']++;
            }
            
            string key = "0:"+to_string(cnt[0]);
            for (int i = 1; i < 26; i++)
            {
                key+=","+to_string(i)+":"+to_string(cnt[i]);
            }
            res[key].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto pair: res)
        {
            ans.push_back(pair.second);
        }
        return ans;

        }
};
