#include <iostream>
using namespace std;
using ll = long long;
ll n, k, t, x, a, b, ans;
ll _pow[100], dp[100];
ll getParent(ll node) { return (node - 2) / k + 1; }
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> k >> t;
    for (ll i = 1; k != 1 && i < n; i *= k) ++x;
    dp[0] = 1;
    _pow[0] = 1;
    for (int i = 1; k != 1 && i <= x; ++i)
    {
        dp[i] = dp[i - 1] * k;
        _pow[i] = dp[i];
    }
    for (int i = 1;  k != 1 && i <= x; ++i)
        dp[i] += dp[i - 1];

    while (t--)
    {
        cin >> a >> b;
        if (k == 1)
        {
            cout << abs(a - b) << '\n';
            continue;
        }
        else if (n == 1)
        {
            cout << 0 << '\n';
            continue;
        }

        if (a < b) swap(a, b);
        ll tx = x;
        ll start = dp[tx - 1] + 1;
        ll end = start + _pow[tx] - 1;
        ans = 0;
        while (!(start <= a && a <= end))
        {
            if (tx - 1 < 0) break;
            start = dp[--tx - 1] + 1;
            end = start + _pow[tx] - 1;
        }
        while (tx != 0 && !(start <= a && a <= end && start <= b && b <= end))
        {
            
            a = getParent(a);
            ans++;
            if (tx - 1 < 0) break;
            start = dp[--tx - 1] + 1;
            end = start + _pow[tx] - 1;
        }
        while (tx != 0 && a != b)
        {
            a = getParent(a);
            b = getParent(b);
            ans += 2;
            if (tx - 1 < 0) break;
            start = dp[--tx - 1] + 1;
            end = start + _pow[tx] - 1;
        }
        cout << ans << '\n';
        
    }
    return 0;
}
