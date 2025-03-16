#include <string>
#include <vector>

using namespace std;
int solution(vector<vector<string>> board, int h, int w) {
    int answer = 0;
    int d[4][2] = {-1, 0, 1, 0, 0, -1, 0, 1};
    for(int i = 0 ; i < 4 ; i++)
        if (0 <= h + d[i][0] && h + d[i][0] < board.size() && 0 <= w + d[i][1] && w + d[i][1] < board[0].size() && board[h + d[i][0]][w + d[i][1]] == board[h][w])answer++;
    return answer;
}