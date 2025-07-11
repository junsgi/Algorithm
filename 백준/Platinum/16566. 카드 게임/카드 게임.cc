#include <iostream>
using namespace std;
#define M 1 << 23
int n, m, k, t, MAX, cnt, seg[M];

int query(int left, int right)
{
    int result = 0;
    --left |= cnt; --right |= cnt;
    while (left <= right)
    {
        if (left & 1) result += seg[left++];
        left >>= 1;
        if (~right & 1) result += seg[right--];
        right >>= 1;
    }
    return result;
}
void update(int idx, int val)
{
    --idx |= cnt;
    seg[idx] = val;
    idx >>= 1;
    while (idx)
    {
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1];
        idx >>= 1;
    }
}
void init()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m >> k;
    for (cnt = 1; cnt < n; cnt <<= 1);
    for (int i = 0; i < m; i++)
    {
        cin >> t;
        update(t, 1);
    }
}
int main()
{
    init();
    while (k--)
    {
        cin >> t;
        int left = t, right = n;
        while (left + 1 < right)
        {
            int mid = (left + right) >> 1;
            if (!query(t + 1, mid)) left = mid;
            else right = mid;
        }
        cout << right << '\n';
        update(right, 0);
    }
    return 0;
}