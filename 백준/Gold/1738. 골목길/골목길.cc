// 유효한 길 설정(메모이제이션) -> 양수 사이클 확인(벨만포드) -> 출력(BFS).
#include<stdio.h>
#include<vector>
#define MAX(x,y)((x)>(y)?(x):(y))
#define M 1<<31
using namespace std;
struct Temp
{
    int s, e, w;
};
int n, m, valid[101], visit[101], cost[101], path[111], que[111], front, rear;
vector<Temp> arr, Rgraph[101];
vector<int> graph[101];
int bellmanford()
{
    for (int i = 1; i <= n; i++)
        cost[i] = M;
    cost[1] = 0;
    int hit = 0;
    for (int i = 0; i < n; i++)
    {
        hit = 0;
        for (Temp& j : arr)
        {
            if (cost[j.s] == M) continue;
            if (cost[j.e] < cost[j.s] + j.w)
            {
                cost[j.e] = cost[j.s] + j.w;
                if (valid[j.s])
                    hit = 1;
            }
        }
    }
    return hit;
}
int memo(int node)
{
    if (valid[node]) return 1;
    for (int tnode : graph[node])
    {
        if (visit[tnode]) continue;
        visit[tnode] = 1;
        valid[node] = MAX(valid[node], memo(tnode));
    }
    return valid[node];
}
void pp(int node)
{
    if (path[node] == -1)
    {
        printf("%d", n);
        return;
    }
    printf("%d ", que[node]);
    pp(path[node]);
}
void answer()
{
    front = rear = -1;
    for (int i = 0; i <= n; i++) 
        visit[i] = 0;
    que[++rear] = n;
    visit[n] = 1;
    path[0] = -1;
    while (front != rear)
    {
        int node = que[++front];
        if (node == 1)
        {
            pp(front);
            return;
        }
        for (Temp i : Rgraph[node])
        {
            int tnode = i.e;
            int weight = i.w;
            if (visit[tnode]) continue;
            if (cost[node] != cost[tnode] + weight) continue;
            que[++rear] = tnode;
            visit[tnode] = 1;
            path[rear] = front;
        }
    }
}
void solution()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        int s, e, w;
        scanf("%d%d%d", &s, &e, &w);
        arr.push_back({ s, e, w });
        graph[s].push_back(e);
        Rgraph[e].push_back({-1, s, w});
    }
    valid[n] = 1;
    visit[1] = 1;
    memo(1); 
    if (!bellmanford())
        answer();
    else
        printf("-1");
}
int main()
{
    solution();
    return 0;
}
