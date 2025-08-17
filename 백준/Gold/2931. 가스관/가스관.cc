#include <iostream>
#include <algorithm>
#include <queue>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
struct Node { int x, y, d; Node(int a, int b, int c) : x{ a }, y{ b }, d{ c } {} };
int n, m, mx, my, md, ex, ey, zx, zy, zd, cnt, visit[25][25];
int dir[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
char map[25][26];
queue<Node*> que;
int inRange(int x, int y) { return 0 <= x && x < n && 0 <= y && y < m; }
Node* nextDir(char& chr, int x, int y, int d)
{
    // |, -, +, 1, 2, 3, 4
    switch (chr)
    {
    case '|':
        if (d <= 1) return new Node(x, y, d);
        break;
    case '-':
        if (1 < d) return new Node(x, y, d);
        break;
    case '1': // r
        if (d == 0) return new Node(x, y, 3);
        else if (d == 2) return new Node(x, y, 1);
        break;
    case '2': // ㄴ
        if (d == 1) return new Node(x, y, 3);
        else if (d == 2) return new Node(x, y, 0);
        break;
    case '3': // J
        if (d == 1) return new Node(x, y, 2);
        else if (d == 3) return new Node(x, y, 0);
        break;
    case '4': // ㄱ
        if (d == 3) return new Node(x, y, 1);
        else if (d == 0) return new Node(x, y, 2);
        break;
    default:
        return nullptr;
    }
    return nullptr;
}
void init()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> map[i];
    md = zd = -1;
    for(int i = 0 ; i < n ; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (map[i][j] == 'M')
            {
                mx = i; my = j;
                for (int k = 0; k < 4; k++)
                {
                    int tx = dir[k][0] + i, ty = dir[k][1] + j;
                    if (!inRange(tx, ty) || map[tx][ty] == '.' || map[tx][ty] == 'Z') continue;
                    md = k;
                    break;
                }
            }
            if (map[i][j] == 'Z')
            {
                zx = i; zy = j;
                for (int k = 0; k < 4; k++)
                {
                    int tx = dir[k][0] + i, ty = dir[k][1] + j;
                    if (!inRange(tx, ty) || map[tx][ty] == '.' || map[tx][ty] == 'M') continue;
                    zd = k;
                    break;
                }
            }
        }
    }
}
void dfs(Node* node)
{
    int tx = dir[node->d][0] + node->x, ty = dir[node->d][1] + node->y;
    if (!inRange(tx, ty)) return;
    if (map[tx][ty] == '.')
    {
        ex = tx; ey = ty;
        return;
    }
    if (visit[tx][ty] == cnt) return;
    visit[tx][ty] = cnt;
    if (map[tx][ty] == '+')
    {
        for (int i = 0; i < 4; i++)
        {
            Node* next_ = new Node(tx, ty, i);
            dfs(next_);
            delete next_;
        }
    }
    else
    {
        Node* next_ = nextDir(map[tx][ty], tx, ty, node->d);
        if (!next_) return;
        dfs(next_);
        delete next_;
    }
}
void findDot()
{
    Node* node;
    if (md != -1)
    {
        node = new Node(mx, my, md);
        visit[mx][my] = ++cnt;
        dfs(node);
        delete node;
    }
    if (zd != -1)
    {
        node = new Node(zx, zy, zd);
        visit[zx][zy] = ++cnt;
        dfs(node);
        delete node;
    }
    //cout << ex << ' ' << ey << ' ';
    
}
int bfs(int sx, int sy, int sd)
{
    que = queue<Node*>();
    que.emplace(new Node(sx, sy, sd));
    visit[sx][sy] = ++cnt;
    int hit = 1;
    while (!que.empty())
    {
        Node* cur = que.front();

        int tx = cur->x + dir[cur->d][0], ty = cur->y + dir[cur->d][1];
        if (!inRange(tx, ty) || map[tx][ty] == '.')
        {
            hit = 0;
            break;
        }

        if (map[tx][ty] == '+' && visit[tx][ty] != cnt)
        {
            visit[tx][ty] = cnt;
            for (int i = 0; i < 4; i++)
                que.emplace(new Node(tx, ty, i));
        }
        else if (map[tx][ty] != '+' && map[tx][ty] != 'Z')
        {
            Node* next_ = nextDir(map[tx][ty], tx, ty, cur->d);
            if (next_ && visit[tx][ty] != cnt)
            {
                que.emplace(next_);
                visit[tx][ty] = cnt;
            }
            else if (!next_)
            {
                hit = 0;
                break;
            }
        }

        delete cur;
        que.pop();
    }
    while (!que.empty())
    {
        delete que.front();
        que.pop();
    }
    return hit;
}
void solution()
{
    findDot();
    const char* arr = "|-+1234";
    for (int i = 0; i < 7; i++)
    {
        map[ex][ey] = arr[i];
        if (bfs(mx, my, md))
        {
            cout << ex + 1 << ' ' << ey + 1 << ' ' << arr[i];
            break;
        }
    }
}
int main()
{
    fastio;
    init();
    solution();
    return 0;
}
/*
5 7
....14.
M---.3.
....|..
....Z..
.......
*/