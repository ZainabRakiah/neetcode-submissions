class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<char>> rows(9);
        vector<vector<char>> cols(9);
        vector<vector<char>> dabba(9);

        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if(board[i][j] == '.'){
                    continue;
                }
                if(find(rows[i].begin(), rows[i].end(), board[i][j]) != rows[i].end()){
                    return false;
                }
                else{ 
                    rows[i].push_back(board[i][j]); 
                }
                if(find(cols[j].begin(), cols[j].end(), board[i][j]) != cols[j].end()){
                    return false;
                }
                else {
                    cols[j].push_back(board[i][j]);
                }
                if(find(dabba[(i/3)*3 + j/3].begin(), dabba[(i/3)*3 + j/3].end(), board[i][j]) != dabba[(i/3)*3 + j/3].end()){
                    return false;
                }
                else{
                    dabba[(i/3)*3 + j/3].push_back(board[i][j]);
                }
            }
        }
        return true;
    }
};