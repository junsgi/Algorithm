/*
다시 제출하샘
역추적 배열 idx를 사용하여 LIS를 출력한다.
순서를 의미하는 x변수
dp 배열의 마지막 원소보다 큰 원소가 오면 idx 배열엔 x값 삽입 후 x++

이분탐색으로 가장 가까운 값의 인덱스를 찾아 현재 값을 끼워 넣는 식이므로 dp 배열의 값이 항상 오름차순이지만 정답이라는 보장은 없다.
idx 배열엔 가까운 값의 인덱스를 push한다.

idx 배열을 거꾸로 순회하여 x 값을 찾았다면 answer배열에 삽입 후 x--
*/
#pragma warning(disable:4996)  
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n, x;
vector<int> arr, dp, idx, ans;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    arr.resize(n);
    idx.resize(n);
    for (int& i : arr) cin >> i;
    for (int i = 0; i < n; i++)
    {
        if (dp.empty() || dp.back() < arr[i])
        {
            dp.push_back(arr[i]);
            idx[i] = x++;
        }
        else
        {
            int res = lower_bound(dp.begin(), dp.end(), arr[i]) - dp.begin();
            dp[res] = arr[i];
            idx[i] = res;
        }
    }
    cout << dp.size() << "\n";
    x--;
    for (int i = idx.size() - 1; i >= 0; i--)
    {
        if (idx[i] == x)
        {
            x--;
            ans.push_back(arr[i]);
        }
    }
    std::reverse(ans.begin(), ans.end());
    for (int& a : ans) cout << a << " ";
    return 0;
}