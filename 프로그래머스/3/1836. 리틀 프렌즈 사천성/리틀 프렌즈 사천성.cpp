#include <string>
#include <string.h>
#include <vector>
#include <iostream>
using namespace std;
struct Temp{
    int x1, y1, x2, y2;
    bool visit;
    Temp(): x1(0), y1(0), x2(0), y2(0), visit(false) {}
}arr[26];
int cnt;
void init(int& m, int& n, vector<string>& board)
{
    int tmp = n; n = m; m = tmp;
    for(int i = 0 ; i < 26 ; i++)arr[i] = {};
    cnt = 0;
    for(int i = 0 ; i < n ; i++)
    {
        for(int j = 0 ; j < m ; j++)
        {
            char target = board[i][j];
            if (!('A' <= target && target <= 'Z')) continue;
            Temp* point = &arr[target - 'A'];
            if (!point->visit)
            {
                cnt++;
                point->visit = true;
                point->x1 = i;
                point->y1 = j;
            }else
            {
                point->x2 = i;
                point->y2 = j;
            }
        }
    }
}
bool check(Temp& t, const vector<string>& board, char ck)
{
    int x = min(t.x1, t.x2), y = min(t.y1, t.y2);
    int n = max(t.x1, t.x2), m = max(t.y1, t.y2);
    bool case1 = true, case2 = true, case3 = true, case4 = true;
    for(int i = x ; i <= n; i++)
    {
        if (board[i][y] != ck && board[i][y] != '.')
            case1 = false;
        if (board[i][m] != ck && board[i][m] != '.')
            case3 = false;
    }
    for(int i = y ; i <= m; i++)
    {
        if (board[x][i] != ck && board[x][i] != '.')
            case2 = false;
        if (board[n][i] != ck && board[n][i] != '.')
            case4 = false;
    }
    if (t.x1 == t.x2) return case2 || case4;
    if (t.y1 == t.y2) return case1 || case3;
    if (t.y1 < t.y2) return (case1 && case4) || (case2 && case3);
    return (case1 && case2) || (case3 && case4);
}
string play(int& n, int& m, vector<string>& board)
{
    bool hit = true;
    string answer = "";
    while(1)
    {
        string res = "";
        while (hit)
        {
            hit = false;
            for(int i = 0 ; i < 26 ; i++)
            {
                if (!arr[i].visit) continue;
                if (check(arr[i], board, 'A' + i))
                {
                    hit = true;
                    arr[i].visit = false;
                    board[arr[i].x1][arr[i].y1] = '.';
                    board[arr[i].x2][arr[i].y2] = '.';
                    res += 'A' + i;
                    break;
                }
            }
        } // hit
        if (res.length() == 0)break;
        answer += res;
    }
    if (answer.length() != cnt) return "IMPOSSIBLE";
    return answer;
}
string solution(int m, int n, vector<string> board) {
    init(m, n, board);
    string answer = play(n, m, board);
    return answer;
}
