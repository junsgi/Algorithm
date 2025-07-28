#include <iostream>
using namespace std;
constexpr long long mod = 1'000'000;
long long n, f[2][2] = { {1, 1}, {1, 0} }, ans[2][2] = { {1, 0}, {0, 1} }, tmp[2][2];
void power(long long(&x)[2][2], long long(&y)[2][2])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            tmp[i][j] = 0;
            for (int k = 0; k < 2; k++)
            {
                tmp[i][j] += (x[i][k] * y[k][j]) % mod;
                tmp[i][j] %= mod;
            }
        }
    }
    for (int i = 0; i < 4; i++) x[i / 2][i % 2] = tmp[i / 2][i % 2];
}
void pro(long long x)
{
    while (x)
    {
        if (x & 1)
            power(ans, f);
        power(f, f);
        x >>= 1;
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n;
    pro(n);
    cout << ans[0][1];
    return 0;
}
