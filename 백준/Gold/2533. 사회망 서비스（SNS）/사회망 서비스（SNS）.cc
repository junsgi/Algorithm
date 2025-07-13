#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int n, dp[1'000'000][2], visit[1'000'000];
vector<int> tree[1'000'000];
void dfs(const int& node)
{
    visit[node] = 1;
    dp[node][1] = 1; // 현재 노드가 얼리어답터일 때
    for (int& tnode : tree[node])
    {
        if (visit[tnode]) continue;
        dfs(tnode);
        // 현재 노드가 일반인일 때 자식 노드들의 얼리어답터 수 ++
        dp[node][0] += dp[tnode][1];

        // 현재 노드가 얼리어답터면 자식이 일반인일때와 얼리어답터일 경우의 수 중 작은 수 ++
        dp[node][1] += min(dp[tnode][0], dp[tnode][1]);
    }
}
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n - 1; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b); a--; b--;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    dfs(0);
    printf("%d", min(dp[0][0], dp[0][1]));
    return 0;
}