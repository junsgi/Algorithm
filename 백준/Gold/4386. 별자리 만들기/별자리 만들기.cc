#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;
struct Node { int x, y; double dis; };
int n, p[100];
double ans;
pair<double, int> x[100], y[100];
vector<Node> arr;
double getDis(double a, double b, double x, double y) 
{
    double ax = abs(a - x); ax *= ax;
    double by = abs(b - y); by *= by;
    return sqrt(ax + by);
}
int find(int node)
{
    if (node == p[node]) return node;
    return p[node] = find(p[node]);
}
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx < fy) p[fy] = fx;
    else if (fx > fy) p[fx] = fy;
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> x[i].first >> y[i].first;
        p[i] = x[i].second = y[i].second = i;
    }
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            arr.push_back({ x[i].second, x[j].second, getDis(x[i].first, y[i].first, x[j].first, y[j].first)});

    sort(arr.begin(), arr.end(), [&](const Node& x, const Node& y) { return x.dis < y.dis; });
    for (const auto& [a, b, dis] : arr)
    {
        if (find(a) == find(b)) continue;
        Union(a, b);
        ans += dis;
    }
    printf("%.2lf", ans);
    return 0;
}
