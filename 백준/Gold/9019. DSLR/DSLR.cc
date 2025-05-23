#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<queue>
#include<string>
#define M 10000
using namespace std;
struct Node 
{
    int n;
    string comm;
    Node(int n, string m) : n(n), comm(m) {}
};
int n, m, target, check[100000], memo[5] = {0, 0, 10, 100, 1000};
queue<Node> que;
int getCnt(int x)
{
    int cnt = 0;
    while (x) { cnt++; x /= 10; }
    return cnt;
}
int L(int x)
{
    int cnt = getCnt(x);
    if (cnt < 4) return x * 10;
    return (x % memo[cnt] * 10) + x / memo[cnt];
}
int R(int x)
{
    return (x / 10) + (x % 10 * 1000);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> m >> target;
        fill(check, check + 100000, 0);
        que = queue<Node>();
        check[m] = 1;
        que.emplace(m, "");
        while (!que.empty())
        {
            Node cur = que.front(); que.pop();
            if (cur.n == target)
            {
                cout << cur.comm << '\n';
                break;
            }

            if (!check[cur.n * 2 % M])
            {
                check[cur.n * 2 % M] = 1;
                que.emplace(cur.n * 2 % M, cur.comm + "D");
            }
            if (!check[cur.n - 1 < 0 ? 9999 : cur.n - 1])
            {
                check[cur.n - 1 < 0 ? 9999 : cur.n - 1] = 1;
                que.emplace(cur.n - 1 < 0 ? 9999 : cur.n - 1, cur.comm + "S");
            }
            if (!check[L(cur.n)])
            {
                check[L(cur.n)] = 1;
                que.emplace(L(cur.n), cur.comm + "L");
            }
            if (!check[R(cur.n)])
            {
                check[R(cur.n)] = 1;
                que.emplace(R(cur.n), cur.comm + "R");
            }
        }
    }
    return 0;
}