#pragma warning(disable:4996)  
#include <iostream>
#include <algorithm>
#include <vector>
#define M 1'000'000'007
using namespace std;
int n, dp[100001][8];
vector<int> graph[8]{ {1, 2}, {0, 2, 3}, {0, 1, 3, 4}, {1, 2, 4, 5}, {2, 3, 5, 6}, {3, 4, 7}, {4, 7}, {5, 6} };
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++)
    {
        int s = 0;
        for (int j = 0; j < 8; j++)
        {
            for (int& node : graph[j])
            {
                dp[i][j] += dp[i - 1][node];
                dp[i][j] %= M;
            }
        }
    }
    cout << dp[n][0];
    return 0;
}