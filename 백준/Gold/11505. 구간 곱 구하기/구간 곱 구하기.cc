#include <iostream>
using namespace std;
constexpr int mod = 1e9+7;
using ll = long long;
int n, m, k, x, a, b;
ll seg[1 << 21], c;
void update(int idx, ll value)
{
    --idx |= x;
    seg[idx] = value;
    while (idx >>= 1)
        seg[idx] = seg[idx << 1] * seg[idx << 1 | 1] % mod;
}
ll query(int st, ll ed)
{
    --st |= x; --ed |= x;
    ll res = 1;
    while (st <= ed)
    {
        if (st & 1)
            res = res * seg[st++] % mod;
        st >>= 1;
        if (!(ed & 1))
            res = res * seg[ed--] % mod;
        ed >>= 1;
    }
    return res;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n >> m >> k;
    for (x = 1; x < n; x *= 2);
    for (int i = 1; i < x; i++) seg[i] = 1;
    for (int i = 1; i <= n; i++)
    {
        cin >> c;
        update(i, c);
    }
    for (int i = 0; i < m + k; i++)
    {
        cin >> a >> b >> c;
        if (a & 1)
            update(b, c);
        else
            cout << query(b, c) << '\n';
    }
    return 0;
}
