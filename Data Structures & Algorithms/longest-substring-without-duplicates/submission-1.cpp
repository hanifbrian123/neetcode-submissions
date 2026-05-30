class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen = 0, l = 0, r = 0;
        unordered_set<char> temp;

        while (r<s.size())
        {
            // cout<< endl<< "R: "<< r<< endl;
            // cout<< "A [ "; this->printSetChar(temp); cout<< "]"<< endl;
            if (temp.find(s[r]) != temp.end()) {
                // cout<< "L: ";
                // cout<< "[ "<< s[l]<< ' '<< s[r] <<" ]";
                while (s[l] != s[r])
                {
                    // cout<< l<< ' ';
                    temp.erase(s[l]);
                    l++;
                }
                l++;
                // cout<< "| Hasil L: "<< l;
                // cout<< endl;
            }
            // cout<< "B [ "; this->printSetChar(temp); cout<< "]"<< endl;
            // cout<< "L, R: "<< l<< ' '<< r<< endl;
            temp.insert(s[r]);
            maxLen = max(r-l+1, maxLen);
            r++;
        }
        return maxLen;
    }
    void printSetChar(unordered_set<char> temp) {
        for (char t: temp)
        {
            cout<< t<< ' ';
        }
    }
};
