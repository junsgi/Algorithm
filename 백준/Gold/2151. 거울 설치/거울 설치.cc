#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int n, sx, sy, visit[4][50][50], dir[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
struct Node
{
    int x, y, d;
    Node(int a, int b, int c) : x{ a }, y{ b }, d{ c } {}
    bool operator>(const Node& other) const {
        return visit[d][x][y] > visit[other.d][other.x][other.y];
    }
};
string map[50];
priority_queue<Node, vector<Node>, greater<Node>> heap;
int inRange(int x, int y) { return 0 <= x && x < n && 0 <= y && y < n; }
pair<int, int> mirror(int x, int y, int d)
{
    if (d <= 1) return { 2, 3 };
    else return { 0, 1 };
}
void init()
{
    fastio;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> map[i];
        for (int j = 0; j < n; j++)
            if (map[i][j] == '#')
                sx = i, sy = j;
    }
}
void solution()
{
    for (int i = 0; i < 4; i++)
    {
        int tx = sx + dir[i][0], ty = sy + dir[i][1];
        if (!inRange(tx, ty) || map[tx][ty] == '*') continue;
        visit[i][sx][sy] = 1;
        heap.emplace(sx, sy, i);
    }
    while (!heap.empty())
    {
        auto [x, y, d] = heap.top();
        heap.pop();
        if ((sx != x || sy != y) && map[x][y] == '#')
        {
            cout << visit[d][x][y] - 1 << '\n';
            break;
        }
        int tx = x + dir[d][0], ty = y + dir[d][1];
        if (!inRange(tx, ty) || map[tx][ty] == '*') continue;
        while (inRange(tx, ty) && map[tx][ty] == '.') { tx += dir[d][0]; ty += dir[d][1]; }

        if (!inRange(tx, ty) || map[tx][ty] == '*') continue;

        if (visit[d][tx][ty] == 0)
        {
            visit[d][tx][ty] = visit[d][x][y];
            heap.emplace(tx, ty, d);
        }
        if (map[tx][ty] == '!')
        {
            auto [a, b] = mirror(tx, ty, d);
            if (visit[a][tx][ty] == 0)
            {
                visit[a][tx][ty] = visit[d][x][y] + 1;
                heap.emplace(tx, ty, a);
            }
            if (visit[b][tx][ty] == 0)
            {
                visit[b][tx][ty] = visit[d][x][y] + 1;
                heap.emplace(tx, ty, b);
            }
        }
    }
}
int main()
{
    {
        init();
        solution();
    }
    
    return 0;
}
/*
a != x && b == y ||
a == x && b != y ||
a != x && b != y
*/