#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
struct Node { int x, y, z; }arr[10000];
int n, m, g[1001], p[1001], c[1001];
int cmp(const Node& x, const Node& y)
{
    return x.z < y.z;
}
int find(int node)
{
    if (p[node] == node) return node;
    return p[node] = find(p[node]);
}
void Union(int x, int y, int z)
{
    int fx = find(x), fy = find(y);
    if (fx == fy) return;
    if (fx < fy)
    {
        p[fy] = fx;
        c[fx] += c[fy] + z;
    }
    else
    {
        p[fx] = fy;
        c[fy] += c[fx] + z;
    }
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
    {
        char a;
        scanf(" %c", &a);
        if (a == 'M') g[i] = 1;
        p[i] = i;
    }
    for (int i = 0; i < m; i++)
        scanf("%d%d%d", &arr[i].x, &arr[i].y, &arr[i].z);
    sort(arr, arr + m, cmp);
    for (int i = 0; i < m; i++)
    {
        if (g[arr[i].x] == g[arr[i].y]) continue;
        Union(arr[i].x, arr[i].y, arr[i].z);
    }
    for (int i = 2; i <= n; i++)
    {
        if (find(i - 1) != find(i))
        {
            printf("-1");
            return 0;
        }
    }
    printf("%d", c[find(1)]);
    return 0;
}
