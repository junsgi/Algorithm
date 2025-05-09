#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
using namespace std;
int n, a, b, p[100001];
vector<int> graph[100001];
void dfs(int node)
{
    for (const int& tnode : graph[node])
    {
        if (p[tnode]) continue;
        p[tnode] = node;
        dfs(tnode);
    }
}
int main()
{
    scanf("%d", &n);
    for (int i = 1; i < n; i++)
    {
        scanf("%d%d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    p[1] = 1;
    dfs(1);
    for (int i = 2; i <= n; i++)
        printf("%d\n", p[i]);
    return 0;
}
