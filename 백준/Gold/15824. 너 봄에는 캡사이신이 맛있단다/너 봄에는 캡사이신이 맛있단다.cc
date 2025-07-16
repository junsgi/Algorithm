#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#define M ((ll)1e9 + 7)
using namespace std;
using ll = long long;
ll n, arr[300'000], ans;
ll p(ll base, int exp)
{
    ll res = 1;
    while (exp)
    {
        if (exp & 1) 
            res = res * base % M;
        base = base * base % M;
        exp >>= 1;
    }
    return res % M;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr, arr + n);
    for (int i = 0; i < n; i++)
    {
        ll mx = p(2, i), mn = p(2, n - i - 1);
        ans += (mx * arr[i] % M) - (mn * arr[i] % M);
        ans = (ans % M + M) % M;
    }
    cout << ans;
    return 0;
}
/*
1. 모든 조합의 MAX - MIN의 합은 (모든 조합의 MAX의 합 - 모든 조합의 MIN의 합)과 같다
[2, 5, 8]의 공집합을 제외한 모든 경우의 수는 다음과 같다
[2], [5], [8], [2, 5], [2, 8], [5, 8], [2, 5, 8]
모든 조합의 최댓값 (2 + 5 + 8 + 5 + 8 + 8 + 8) - 모든 조합의 최솟값(2 + 5 + 8 + 2 + 2 + 5 + 2)

정렬하여 최솟값을 가장 앞으로 최댓값을 가장 뒤로 배치한다.
arr[i]가 조합 중 가장 클 때 나올 수 있는 경우의 수는 2^i개이다.
arr[i]가 조합 중 가장 작을 때 나올 수 있는 경우의 수는 2^n-i-1개이다.

따라서 점화식은 (arr[i] * 2^i) - (arr[i] * 2^n-i-1)
거듭제곱은 따로 배열에 구해놓거나 logN만에 구한다.
*/