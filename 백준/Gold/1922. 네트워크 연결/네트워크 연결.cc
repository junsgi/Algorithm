#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
struct Temp {
    int st, ed, w;
};
int n, m, p[1001], answer;
vector<Temp> arr;
int cmp(Temp& a, Temp& b) { return a.w < b.w; }
void init()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
        p[i] = i;
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        arr.push_back({ a, b, c });
    }
}
int find(int x)
{
    if (p[x] == x) return x;
    return p[x] = find(p[x]);
}
int Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    int res = fx == fy;
    if (fx < fy)
        p[fy] = fx;
    else if (fx > fy)
        p[fx] = fy;
    return res;
}
void solution()
{
    sort(arr.begin(), arr.end(), cmp);
    for (Temp& i : arr)
    {
        if (Union(i.st, i.ed)) continue;
        answer += i.w;
    }
    printf("%d", answer);
}
int main()
{
    init();
    solution(); // 최소 신장 트리
    return 0;
}