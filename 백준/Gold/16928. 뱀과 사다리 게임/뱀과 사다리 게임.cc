#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;
int n, m, a, b, s[101], visit[101];
priority_queue<pair<int, int>> que;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for (int i = 0; i < n + m; i++)
    {
        cin >> a >> b;
        s[a] = b;
    }
    que.push({1, 1});
    visit[1] = 1;
    while (!que.empty())
    {
        pair<int ,int> cur = que.top(); que.pop();
        if (cur.second == 100)
        {
            cout << -cur.first - 1;
            break;
        }
        if (s[cur.second] != 0)
        {
            visit[s[cur.second]] = visit[cur.second];
            que.push({ -visit[s[cur.second]], s[cur.second] });
            continue;
        }
        for (int i = 1; i <= 6; i++)
        {
            if (visit[cur.second + i]) continue;
            visit[cur.second + i] = visit[cur.second] + 1;
            que.push({ -visit[cur.second + i], cur.second + i });
        }
    }
    return 0;
}

/*
2 1
2 60
21 99
61 20
*/