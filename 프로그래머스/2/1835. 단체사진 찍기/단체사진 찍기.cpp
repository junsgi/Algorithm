#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int idx[26] = {0, }, c[8] = {}, visit[8] = {-1, -1, -1, -1, -1, -1, -1, -1}, answer;
char name[9] = "ACFJMNRT";
vector<string> commands;
bool check()
{
    for(int i = 0 ; i < 8 ; i++)
    {
        idx[name[i] - 65] = visit[i];
    }
    for(int i = 0 ; i < commands.size() ; i++)
    {
        int dist = abs(idx[commands[i][0] - 65] - idx[commands[i][2] - 65]) - 1;
        int c = commands[i][4] - '0';
        if (commands[i][3] == '=' && dist != c)
            return false;
        if (commands[i][3] == '>' && dist <= c)
            return false;
        if (commands[i][3] == '<' && dist >= c)
            return false;
    }
    return true;
}
void p(int depth)
{
    if (depth == 8)
    {
        if (check())
            answer++;
        return;
    }
    for(int i = 0 ; i < 8 ; i++)
    {
        if(c[i]) continue;
        c[i] = 1;
        visit[depth] = i;
        p(depth + 1);
        c[i] = 0;
        visit[depth] = 0;
    }
}
int solution(int n, vector<string> data) {
    commands = data;
    answer = 0;
    p(0);
    return answer;
}