#include <iostream>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
constexpr int m = 100'000;
int n, k, visit[200'001], que[200'111], front, rear, path[200'111];
void p(int node)
{
    if (node == -1) return;
    p(path[node]);
    cout << que[node] << ' ';
}
int main()
{
    fastio;
    cin >> n >> k;
    if (n >= k)
    {
        cout << n - k << '\n';
        for (int i = n; i >= k; --i)
            cout << i << ' ';
        return 0;
    }
    front = rear = -1;

    que[++rear] = n;
    path[rear] = -1;
    visit[n + m] = 1;
    while (front != rear)
    {
        int cur = que[++front];
        int depth = visit[cur + m];
        if (cur == k)
        {
            cout << depth - 1 << '\n';
            p(front);
            break;
        }
        if (0 <= (cur << 1) + m && (cur << 1) + m <= 200'000 && visit[(cur << 1) + m] == 0)
        {
            visit[(cur << 1) + m] = depth + 1;
            que[++rear] = (cur << 1);
            path[rear] = front;
        }
        if (m <= cur - 1 + m && visit[cur - 1 + m] == 0)
        {
            visit[cur - 1 + m] = depth + 1;
            que[++rear] = cur - 1;
            path[rear] = front;
        }
        if (0 <= cur + 1 + m && cur + 1 + m <= 200'000 && visit[cur + 1 + m] == 0)
        {
            visit[cur + 1 + m] = depth + 1;
            que[++rear] = cur + 1;
            path[rear] = front;
        }
        
    }
    return 0;
}
