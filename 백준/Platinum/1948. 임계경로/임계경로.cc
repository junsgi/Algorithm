// 위상 정렬로 만나는 시간을 구함 + (각 도시마다 마지막으로 도착한 시간을 구함)
// BFS로 목적지에서 출발지로 쉬지 않고 달려야 하는 도로의 수를 구함
#include<stdio.h>
#include<vector>
#define MAX(x,y)((x)<(y)?(y):(x))
using namespace std;
struct Temp { int node, w; };
int n, m, check[10'001], cost[10'001], st, ed, que[11111], front, rear;
vector<Temp> graph[10'001], re[10'001];
void init()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        graph[a].push_back({ b, c });
        re[b].push_back({ a, c });
        check[b]++;
    }
    scanf("%d%d", &st, &ed);
}
void topologicalSort()
{
    front = rear = -1;
    que[++rear] = st;
    while (front != rear)
    {
        int el = que[++front];
        for (Temp& i : graph[el])
        {
            cost[i.node] = MAX(cost[i.node], cost[el] + i.w);
            if (--check[i.node] == 0)
                que[++rear] = i.node;
        }
    }
    printf("%d\n", cost[ed]);
}
void bfs()
{
    int cnt = 0;
    front = rear = -1;
    que[++rear] = ed;
    check[ed] = 1;
    while (front != rear)
    {
        int node = que[++front];
        for (Temp& i : re[node])
        {
            if (cost[node] != cost[i.node] + i.w) continue;
            cnt++;
            if (check[i.node]) continue;
            check[i.node] = 1;
            que[++rear] = i.node;
        }
    }
    printf("%d", cnt);
}
int main()
{
    init();
    topologicalSort();
    bfs();
    return 0;
}