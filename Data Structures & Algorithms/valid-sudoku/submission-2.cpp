class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        // Optimize solution
        bool ret = true;
        vector<vector<map<char, int>>> cnt3(3, vector<map<char, int>>(3));
        for (int i = 0; i < 9; i++)
        {
            map<char, int> cnt1;
            map<char, int> cnt2;
            for (int j = 0; j < 9; j++)
            {
                char currSide = board[i][j];
                char currDown = board[j][i];

                if (currSide != '.') {
                    if ( cnt1.count(currSide) > 0 ) {
                        ret =  false;
                    }
                    cnt1[currSide]++;

                    if (cnt3[i/3][j/3].count(currSide) > 0) {
                        ret =  false;
                    }
                    cnt3[i/3][j/3][currSide]++;
                }
                if (currDown != '.') {
                    if ( cnt2.count(currDown) > 0 ) {
                        ret =  false;
                    }
                    cnt2[currDown]++;
                }
            }
        }

        return ret;
    }
};