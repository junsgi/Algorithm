#include <iostream>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int main()
{
    fastio;
    int n;
    long long ans;
    cin >> n;
    ans = 0;
    for (int k = 1; k <= n; k++)
        ans += k * (n / k);

    cout << ans;
    return 0;
}
