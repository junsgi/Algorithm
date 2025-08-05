#include <iostream>
#include <iomanip>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int n, m, memory[101], cost[101], dp[101][10001], ans;
int main()
{
    fastio;
    
    cin >> n >> m;
    for (int i = 1; i <= n; i++) cin >> memory[i];
    for (int i = 1; i <= n; i++) cin >> cost[i];
    ans = 0x7fffffff;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= 10001; j++)
        {
            dp[i][j] = dp[i - 1][j];
            if (j - cost[i] >= 0)
                dp[i][j] = max(dp[i][j], dp[i - 1][j - cost[i]] + memory[i]);
            if (dp[i][j] >= m)
                ans = min(ans, j);
        }
    }
    cout << ans;
    return 0;
}