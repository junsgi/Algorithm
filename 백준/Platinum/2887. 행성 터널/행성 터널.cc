#pragma warning(disable:4996)  
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
struct Node
{
    int a, b, c;
    Node() {}
    Node(int x, int y, int z) : a{ x }, b{ y }, c{ z } {}
};
int n, p[100000], ans;
vector<pair<int, int>> X, Y, Z;
vector<Node> res;
int find(int x) { return x == p[x] ? x : p[x] = find(p[x]); }
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx == fy) return;
    p[fx] = fy;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    X.resize(n); Y.resize(n), Z.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin >> X[i].first >> Y[i].first >> Z[i].first;
        p[i] = X[i].second = Y[i].second = Z[i].second = i;
    }
    sort(X.begin(), X.end()); sort(Y.begin(), Y.end()); sort(Z.begin(), Z.end());
    for (int i = 0; i < n - 1; i++)
    {
        res.push_back({ X[i].second, X[i + 1].second, X[i + 1].first - X[i].first });
        res.push_back({ Y[i].second, Y[i + 1].second, Y[i + 1].first - Y[i].first });
        res.push_back({ Z[i].second, Z[i + 1].second, Z[i + 1].first - Z[i].first });
    }
    sort(res.begin(), res.end(), [&](const Node& x, const Node& y) {return x.c < y.c;});
    for (auto& [a, b, c] : res)
    {
        if (find(a) == find(b)) continue;
        Union(a, b);
        ans += c;
    }
    cout << ans;
    return 0;
}