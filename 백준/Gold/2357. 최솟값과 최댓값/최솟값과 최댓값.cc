#pragma warning(disable:4996)
#include <iostream>
#define M ((int)1e9 + 1)
using namespace std;
int n, m, x, t1, t2, mx[1 << 18], mn[1 << 18];
int min(int x, int y) { return x < y ? x : y; }
int max(int x, int y) { return x < y ? y : x; }
void update(int idx, int value, int(&seg)[1 << 18], int (&func)(int, int))
{
    --idx |= x;
    seg[idx] = value;
    idx >>= 1;
    while (idx)
    {
        seg[idx] = func(seg[idx * 2], seg[idx * 2 + 1]);
        idx >>= 1;
    }
}
int query(int st, int ed, int(&seg)[1 << 18], int(&func)(int, int))
{
    int res = 0;
    if (func(1, 2) == 1) res = M;

    --st |= x; --ed |= x;
    while (st <= ed)
    {
        if (st & 1) { res = func(res, seg[st++]); }
        st >>= 1;
        if (~ed & 1) { res = func(res, seg[ed--]); }
        ed >>= 1;
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n >> m;
    for (x = 1; x < n; x *= 2);
    fill(mn, mn + x * 2, M);
    for (int i = 1; i <= n; i++)
    {
        cin >> t1;
        update(i, t1, mx, max);
        update(i, t1, mn, min);
    }
    for (int i = 0; i < m; i++)
    {
        cin >> t1 >> t2;
        cout << query(t1, t2, mn, min) << ' ' << query(t1, t2, mx, max) << '\n';
    }
    return 0;
}
