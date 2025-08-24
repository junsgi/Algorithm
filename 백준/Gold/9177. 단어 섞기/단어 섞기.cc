#include <iostream>
#include <string>
#include <algorithm>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int n, dp[201][201];
string a, b, target;
bool memo(int i, int j)
{
    if (i == a.size() && j == b.size()) return true;
    if (dp[i][j] != -1) return dp[i][j];
    if (i < a.size() && a[i] == target[i + j] && memo(i + 1, j)) return dp[i][j] = true;
    if (j < b.size() && b[j] == target[i + j] && memo(i, j + 1)) return dp[i][j] = true;
    return dp[i][j] = false;
}
int main()
{
    fastio;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a >> b >> target;
        fill(&dp[0][0], &dp[0][0] + 201 * 201, -1);
        cout << "Data set " << i << ": " << (memo(0, 0) ? "yes" : "no") << '\n';
    }
    return 0;
}
