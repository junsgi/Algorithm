#include <iostream>
#include <algorithm>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
struct Node{
    int sx, sy, ex, ey;
    Node() :sx{ 0 }, sy{ 0 }, ex{ 0 }, ey{ 0 } {}
    Node(int a, int b, int c, int d) : sx(a), sy(b), ex(c), ey(d) {}
}arr[1001];
int n, p[1001], visit[1001];
int ccw(int a, int b, int c, int d, int e, int f)
{
    int res = (a * d + c * f + e * b) - (c * b + e * d + a * f);
    if (res < 0) return -1;
    else if (res > 0) return 1;
    return 0;
}
int find(int node)
{
    if (node == p[node]) return node;
    return p[node] = find(p[node]);
}
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx < fy)
        p[fy] = fx;
    else if (fx > fy)
        p[fx] = fy;
}
Node* make_loc(const Node& origin) {
    Node* arr = new Node[4];
    auto& [x1, y1, x2, y2] = origin;
    arr[0] = Node(x1, y1, x1, y2); // 왼쪽 변
    arr[1] = Node(x1, y2, x2, y2); // 위쪽 변
    arr[2] = Node(x2, y1, x2, y2); // 오른쪽 변
    arr[3] = Node(x1, y1, x2, y1); // 아래쪽 변
    return arr;
}
void init()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        arr[i] = { a, b, c, d };
        p[i] = i;
    }
}
int process(const Node* const x, const Node* const y)
{
    for (int i = 0; i < 4; i++)
    {
        auto [isx, isy, iex, iey] = x[i];
        for (int k = 0; k < 4; k++)
        {
            auto [ksx, ksy, kex, key] = y[k];

            int case1 = ccw(isx, isy, iex, iey, ksx, ksy) * ccw(isx, isy, iex, iey, kex, key);
            int case2 = ccw(ksx, ksy, kex, key, isx, isy) * ccw(ksx, ksy, kex, key, iex, iey);

            if (case1 == 0 && case2 == 0)
            {
                int res = min(isx, iex) <= max(ksx, kex) && 
                    min(ksx, kex) <= max(isx, iex) && 
                    min(isy, iey) <= max(ksy, key) && 
                    min(ksy, key) <= max(isy, iey);

                if (res)
                    return 1;
            }
            else if (case1 <= 0 && case2 <= 0)
                return 1;
        }
    }
    return 0;
}
void solution()
{
    Node** loc = new Node*[1001];
    loc[0] = new Node[4]; // (0, 0) 좌표
    for (int i = 1; i <= n; i++)
        loc[i] = make_loc(arr[i]);

    for (int i = 0; i <= n; i++)
    {
        for (int j = i + 1; j <= n; j++)
        {
            if (process(loc[i], loc[j]))
                Union(i, j);
        }
        delete[] loc[i];
    }
    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        int fi = find(i);
        if (fi != 0 && visit[fi] == 0)
        {
            visit[fi] = 1;
            ans++;
        }
    }
    cout << ans;
    delete[] loc;
}
int main()
{
    init();
    solution();
    return 0;
}