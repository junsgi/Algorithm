#include<iostream>
#include<algorithm>
using namespace std;
int n, m, a[500'000], b[500'000], ans[500'000];
int binary_s(int target)
{
    int left = 0, right = m - 1;
    while (left <= right)
    {
        int mid = left + right >> 1;
        if (b[mid] < target) left = mid + 1;
        else if (b[mid] > target) right = mid - 1;
        else return 1;
    }
    return 0;
}
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];
    sort(a, a + n);
    sort(b, b + m);
    int cnt = 0;
    for (int i = 0; i < n; ++i)
        if (!binary_s(a[i]))
            ans[cnt++] = a[i];
    cout << cnt;
    if (cnt) cout << '\n';
    for (int i = 0; i < cnt; ++i)
        cout << ans[i] << ' ';
    return 0;
}