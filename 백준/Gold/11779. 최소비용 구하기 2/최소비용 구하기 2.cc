#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#define M 500000000
using namespace std;
int n, m, k, s, e, cost[1001], graph[1001][1001], path[1000], visit[1001];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
int dfs(int node, int depth)
{
    path[k++] = node;
    if (node == s) return depth;
    visit[node] = 1;
    for (int i = 1; i <= n; i++)
    {
        if (visit[i]) continue;
        if (cost[node] != cost[i] + graph[i][node]) continue;
        return dfs(i, depth + 1);
    }
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) 
    {
        cost[i] = M;
        for (int j = 1; j <= n; j++)
            graph[i][j] = M;
    }
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        graph[a][b] = min(graph[a][b], c);
    }
    scanf("%d%d", &s, &e);
    heap.push({ 0, s });
    cost[s] = 0;
    while (!heap.empty())
    {
        pair<int, int> c = heap.top(); heap.pop();
        int node = c.second;
        int weight = c.first;
        if (cost[node] < weight) continue;
        for(int i = 1 ; i <= n ; i++)
        {
            int tnode = i, tw = graph[node][tnode];
            if (cost[tnode] <= cost[node] + tw) continue;
            cost[tnode] = cost[node] + tw;
            heap.push({ cost[tnode], tnode });
        }
    }
    printf("%d\n%d\n", cost[e], dfs(e, 0) + 1);
    for (int i = k - 1; i >= 0; i--)
        printf("%d ", path[i]);
    return 0;
}
