#pragma warning(disable:4996)  
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n;
vector<int> arr, dp;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    arr.resize(n);
    for (int& i : arr) cin >> i;
    for (int i = 0; i < n; i++)
    {
        if (dp.empty() || dp.back() < arr[i])
            dp.push_back(arr[i]);
        else
        {
            int idx = lower_bound(dp.begin(), dp.end(), arr[i]) - dp.begin();
            dp[idx] = arr[i];
        }
    }
    cout << dp.size() << "\n";
    return 0;
}