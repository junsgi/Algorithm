#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, m, k, ans, p[500001];
int find(int node)
{
    if (node == p[node]) return node;
    return p[node] = find(p[node]);
}
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx != fy)
        p[fx] = fy;
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i <= n; i++) p[i] = i;
    while (m--)
    {
        scanf("%d", &k);
        k = find(k);
        if (k == 0) break;
        ans++;
        Union(k, k - 1);
    }
    printf("%d", ans);
    return 0;
}