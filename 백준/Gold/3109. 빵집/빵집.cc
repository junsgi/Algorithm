#include<iostream>
#include<string>
using namespace std;
int n, m, visit[10'000][500];
string graph[10'000];
void input()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    for (int i = 0; i < n; ++i) cin >> graph[i];
}
int inRange(int x, int y) { return 0 <= x && x < n && 0 <= y && y < m; }
int dfs(int x, int y)
{
    visit[x][y] = 1;
    if (y == m - 1) return 1;
    if (inRange(x - 1, y + 1) && !visit[x - 1][y + 1] && graph[x - 1][y + 1] != 'x')
        if (dfs(x - 1, y + 1)) return 1;
    if (inRange(x, y + 1) && !visit[x][y + 1] && graph[x][y + 1] != 'x')
        if (dfs(x, y + 1)) return 1;
    if (inRange(x + 1, y + 1) && !visit[x + 1][y + 1] && graph[x + 1][y + 1] != 'x')
        if (dfs(x + 1, y + 1)) return 1;
    return 0;
}
void solution()
{
    int ans = 0;
    for (int i = 0; i < n; ++i)
        ans += dfs(i, 0);
    cout << ans;
}
int main()
{
    input();
    solution();
    return 0;
}