// 내 원수끼리는 친구가 포인트
// 원수 정보를 따로 저장하여 원수들끼리 UNION
#include<stdio.h>
#include<vector>
using namespace std;
int n, m, b, c;
char a;
int q[1001];
vector<int> graph[1001];
int find(int x)
{
    if (q[x] == x) return x;
    return q[x] = find(q[x]);
}
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx == fy) return;
    if (fx < fy) q[fy] = fx;
    else q[fx] = fy;
}
int main()
{
    int answer = 0;
    scanf("%d", &n);
    scanf("%d", &m);
    for (int i = 0; i <= n; i++)q[i] = i;
    for (int i = 0; i < m; i++)
    {
        scanf(" %c%d%d", &a, &b, &c);
        if (a == 'F')
            Union(b, c);
        else
        {
            graph[b].push_back(c);
            graph[c].push_back(b);
        }
    }
    for (int i = 1; i <= n; i++)
    {
        if (graph[i].size() < 2) continue;
        for (int j = 1; j < graph[i].size(); j++)
            Union(graph[i][j - 1], graph[i][j]);
    }
    for (int i = 1; i <= n; i++)
        if (q[i] == i) answer++;
    printf("%d", answer);
    return 0;
}