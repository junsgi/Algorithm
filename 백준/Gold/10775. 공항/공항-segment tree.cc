#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, m, c, k, ans, seg[1 << 20];
int insert(int left, int right, int idx, int target, int value = -1)
{
    if (target < left || right < target) return seg[idx];
    if (left == right && left == target)
        return seg[idx] = value;
    int mid = (left + right) / 2;
    int l = insert(left, mid, idx * 2, target, value);
    int r = insert(mid + 1, right, idx * 2 + 1, target, value);
    return seg[idx] = max(l, r);
}
int query(int left, int right, int idx, int st, int ed)
{
    if (ed < left || right < st) return -1;
    if (st <= left && right <= ed) return seg[idx];
    int mid = (left + right) / 2;
    int l = query(left, mid, idx * 2, st, ed);
    int r = query(mid + 1, right, idx * 2 + 1, st, ed);
    return max(l, r);
}
int main()
{
    scanf("%d%d", &n, &m);
    for (c = 1; c < n; c *= 2);
    for (int i = 1; i <= n; i++)
        insert(1, c, 1, i, i);
    while (m--)
    {
        scanf("%d", &k);
        int res = query(1, c, 1, 1, k);
        if (res == -1) break;
        insert(1, c, 1, res, -1);
        ans++;
    }
    printf("%d", ans);
    return 0;
}
