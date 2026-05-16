class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        // Samping
        for (int i = 0; i < 9; i++)
        {
            map<char, int> cnt;
            for (int j = 0; j < 9; j++)
            {
                if (board[i][j] != '.') {
                    if ( cnt.count(board[i][j]) > 0) {
                        return false;
                    }
                    cnt[board[i][j]]++;
                }
            }
        }

        // Ke bawah
        for (int i = 0; i < 9; i++)
        {
            map<char, int> cnt;
            for (int j = 0; j < 9; j++)
            {
                char curr = board[j][i];
                if (curr!='.') {
                    if ( cnt.count(curr) > 0) {
                        return false;
                    }
                    cnt[curr]++;
                }
            }
        }

        // kotak-kotak
        vector<vector<map<char, int>>> cnt(3, vector<map<char, int>>(3));
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                char curr = board[i][j];
                if (curr!='.') {
                    if (cnt[(i)/3][(j)/3].count(curr) > 0) {
                        return false;
                    }
                    cnt[(i)/3][(j)/3][curr]++;
                }
            }
        }
        

        

        return true;
    }
};