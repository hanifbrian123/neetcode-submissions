class Solution {
public:

    string encode(vector<string>& strs) {
        int n = strs.size();
        string res = to_string(n)+"|";
        for (int i = 0; i < n; i++)
        {
            res += to_string(strs[i].size())+"|"+strs[i];
        }
        return res;
    }

    vector<string> decode(string s) {
        string sN = "";
        int i = 0;
        while (s[i] != '|')
        {
            sN += s[i];
            i++;
        }
        int n = stoi(sN);
        
        vector<string> res;
        int cnt = 0; 
        i++;
        while (cnt<n)
        {
            string sL = "";
            while (s[i]!='|')
            {
                sL += s[i];
                i++;
            }
            int l = stoi(sL);
            i++;
            string temp = "";
            for (int j = 0; j < l; j++)
            {
                temp += s[i];
                i++;
            }
            res.push_back(temp);
            cnt++;
        }
        return res;
    }
};