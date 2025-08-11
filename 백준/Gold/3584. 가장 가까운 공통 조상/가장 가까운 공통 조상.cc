#include <iostream>
#include <iomanip>
#include <vector>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int t, n, k, depth[10001], check[10001], dp[15][10001], que[10011];
vector<int> map[10001];
void bfs()
{
    int front = -1, rear = -1;
    for (int i = 1; i <= n; i++)
    {
        if (!check[i])
        {
            que[++rear] = i;
            break;
        }
    }
    while (front != rear)
    {
        int node = que[++front];
        for (int& tnode : map[node])
        {
            dp[0][tnode] = node;
            depth[tnode] = depth[node] + 1;
            que[++rear] = tnode;
        }
    }
}
int main()
{
    fastio;
    cin >> t;
    while(t--)
    {
        cin >> n;
        for (int i = 1; i < n; i <<= 1) k++;

        int a, b;
        for (int i = 1; i < n; i++)
        {
            cin >> a >> b;
            map[a].push_back(b);
            check[b]++;
        }
        bfs();
        for (int i = 1; i <= k; ++i)
            for (int j = 1; j <= n; ++j)
                dp[i][j] = dp[i - 1][dp[i - 1][j]];
        cin >> a >> b;
        if (depth[a] < depth[b]) // b가 깊이가 더 깊다면 swap
            swap(a, b);
        int diff = depth[a] - depth[b];
        for (int i = k; i >= 0; --i)
        {
            if (diff & (1 << i))
                a = dp[i][a];
        }
        while (a != b)
        {
            for (int i = k; i >= 0; --i)
            {
                if (dp[i][a] != dp[i][b])
                {
                    a = dp[i][a];
                    b = dp[i][b];
                }
            }
            if (dp[0][a] == dp[0][b])
            {
                a = dp[0][a];
                break;
            }
        }
        cout << a << '\n';
        for (int i = 0; i <= n; ++i)
        {
            check[i] = depth[i] = 0;
            map[i].clear();
            for (int j = 0; j <= k; ++j) dp[j][i] = 0;
        }
        k = 0;
    }
    return 0;
}
