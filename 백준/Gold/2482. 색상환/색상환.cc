#include <iostream>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
constexpr int mod = 1e9 + 3;
int n, k, dp[1000][1001];
int memo(int depth, int cnt)
{
    if (cnt == k) return 1; // 성공했다면 경우의 수 1 추가
    if (depth >= n || n - depth - 1 < k - cnt) return 0;
    int& res = dp[depth][cnt];
    if (res != -1) return res;
    res = 0;
    res += memo(depth + 2, cnt + 1); // 고른다
    res %= mod;
    res += memo(depth + 1, cnt); // 안 고른다.
    res %= mod;
    return res;
}
int main()
{
    fastio;
    cin >> n >> k;
    fill(&dp[0][0], &dp[0][0] + 1000 * 1001, -1);
    cout << (memo(0, 0) + memo(2, 1)) % mod;
    return 0;
}
