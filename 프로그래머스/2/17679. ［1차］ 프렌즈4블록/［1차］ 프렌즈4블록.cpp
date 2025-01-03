#include <string>
#include <vector>
#include <iostream>
using namespace std;
int check[30][30];
void erase(int& n, int& m, vector<string>& board, int cnt)
{
    for(int i = 0 ; i <= n - 2 ; i++)
    {
        for(int j = 0 ; j <= m - 2 ; j++)
        {
            if (board[i][j] == '.') continue;
            if (board[i][j] == board[i][j + 1] && 
               board[i + 1][j] == board[i + 1][j + 1] &&
               board[i][j] == board[i + 1][j])
            {
                check[i][j] = cnt;
                check[i][j + 1] = cnt;
                check[i + 1][j] = cnt;
                check[i + 1][j + 1] = cnt;
            }
        }
    }
}
void compaction(vector<string>& board)
{
    for(int j = 0 ; j < board[0].length() ; j++)
    {
        for(int i = board.size() - 1 ; i >= 0 ; i--)
        {
            if (board[i][j] != '.') continue;
            for(int z = i - 1; z >= 0 ; z--)
            {
                if (board[z][j] == '.') continue;
                board[i][j] = board[z][j];
                board[z][j] = '.';
                break;
            }
        }
    }
}
int solution(int m, int n, vector<string> board) {
    int answer = 0;
    int tmp = m;
    m = n; n = tmp;
    int cnt = 0;
    while(1)
    {
        erase(n, m, board, ++cnt);
        
        int c = 0;
        for(int i = 0 ; i < n ; i++)
        {
            for(int j = 0 ; j < m ; j++)
            {
                if (check[i][j] == cnt)
                {
                    c++;
                    board[i][j] = '.';
                }
            }
        }
        if (c == 0) break;
        else answer += c;
        compaction(board);
    }
    return answer;
}