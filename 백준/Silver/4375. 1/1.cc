#include <iostream>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int main()
{
    fastio;
    int n, k, ans;
    while (cin >> n)
    {
        k = 1;
        ans = 1;
        while (1)
        {
            if (ans % n == 0)
                break;
            else
            {
                ++k;
                ans = ans * 10 | 1;
                ans %= n;
            }
        }
        cout << k << '\n';
    }
    return 0;
}
