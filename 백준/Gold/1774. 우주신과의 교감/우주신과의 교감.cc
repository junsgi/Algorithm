#pragma warning(disable:4996)
#include <stdio.h>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
struct Node { int a, b; double dist; };
int n, m, p[1000];
double x[1000], y[1000], ans;
vector<Node> arr;
double dist(int i, int j)
{
    double dx = abs(x[i] - x[j]); dx *= dx;
    double dy = abs(y[i] - y[j]); dy *= dy;
    return sqrt(dx + dy);
}
int find(int node)
{
    if (node == p[node]) return node;
    return p[node] = find(p[node]);
}
void Union(int a, int b)
{
    int fa = find(a), fb = find(b);
    if (fa < fb) p[fb] = fa;
    else if (fa > fb) p[fa] = fb;
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
    {
        scanf("%lf%lf", &x[i], &y[i]);
        p[i] = i;
    }
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        scanf("%d%d", &a, &b); --a; --b;
        Union(a, b);
    }
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            arr.push_back({ i, j, dist(i, j) });
    sort(arr.begin(), arr.end(), [&](const Node& x, const Node& y) { return x.dist < y.dist; });
    for (const auto& [a, b, d] : arr)
    {
        if (find(a) == find(b)) continue;
        ans += d;
        Union(a, b);
    }
    printf("%.2lf", ans);
    return 0;
}
