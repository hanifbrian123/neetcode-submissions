class Solution {
public:
    bool isValid(string s) {
        string opB = "({[";
        string clB = ")}]";
        vector<char> st;
        st.push_back(s[0]);
        for (int i = 1; i < s.size(); i++)
        {
            cout<< endl;
            for (auto a: st)
            {
                cout<< a<< ' ';
            }
            cout<< endl;

            char curr = s[i];
            cout<< curr;
            if (find(opB.begin(), opB.end(), curr)!=opB.end()) {
                st.push_back(curr);
            } else {
                int idxOp = find(opB.begin(), opB.end(), st[st.size()-1]) - opB.begin();
                int idxCl = find(clB.begin(), clB.end(), curr) - clB.begin();
                cout<< idxOp<< ' '<< idxCl<< endl;
                if (find(clB.begin(), clB.end(), st[st.size()-1]) != clB.end()) {
                    return false;
                } else if (idxOp!=idxCl) {
                    return false;
                } else {
                    st.pop_back();
                }
            }

            
        }
        return st.empty();
    }
};