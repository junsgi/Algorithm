#pragma warning(disable:4996)
#include <iostream>
using namespace std;
using pii = pair<int, int>;
constexpr int M = 1e9 + 1;
int n, x, ix[1 << 18], a, b, c;
pii seg[1 << 18];
void update(int idx, int value)
{
    c = idx;
    --idx |= x;
    seg[idx] = { value, c };
    while (idx >>= 1)
        seg[idx] = min(seg[idx << 1], seg[idx << 1 | 1]);
}
int query(int st, int ed)
{
    pii res = {M, M};
    --st |= x; --ed |= x;
    while (st <= ed)
    {
        if (st & 1) res = min(res, seg[st++]);
        st >>= 1;
        if (~ed & 1) res = min(res, seg[ed--]);
        ed >>= 1;
    }
    return res.second;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n;
    for (x = 1; x < n; x <<= 1);
    fill(seg, seg + (x << 1), make_pair(M, M));
    for (int i = 1; i <= n; i++)
    {
        cin >> a;
        update(i, a);
    }
    cin >> n;
    while (n--)
    {
        cin >> a >> b >> c;
        if (a & 1)
            update(b, c);
        else
            cout << query(b, c) << '\n';
    }
    return 0;
}
