#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
int n, m, s, c, p[100001];
struct Node { int x, y, z; };
vector<Node> arr;
int cmp(const Node& x, const Node& y)
{
    return x.x < y.x || x.x == y.x && x.y > y.y;
}
int find(int node)
{
    if (node == p[node]) return node;
    return p[node] = find(p[node]);
}
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx == fy) return;
    if (fx < fy)
        p[fy] = fx;
    else
        p[fx] = fy;
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        arr.push_back({ a, 1, i });
        arr.push_back({ b, -1, i });
        p[i] = i;
    }

    sort(arr.begin(), arr.end(), cmp);
    s = 1;
    for (int i = 1; i < arr.size(); i++)
    {
        if (arr[i].y == 1 && s > 0)
            Union(arr[i - 1].z, arr[i].z);
        s += arr[i].y;
    }
    for (int i = 0; i < m;i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        if (find(a) == find(b))
            printf("1\n");
        else
            printf("0\n");
    }
    return 0;
}
