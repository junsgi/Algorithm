#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#define M 1'000'000'007;
using namespace std;
using ll = long long;
ll n, ans[2][2] = { {1, 0}, {0, 1} }, m[2][2] = { {1, 1}, {1, 0} }, tmp[2][2];
void pow(ll(&x)[2][2], ll(&y)[2][2])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            tmp[i][j] = 0;
            for (int k = 0; k < 2; k++)
            {
                tmp[i][j] += (x[i][k] * y[k][j]) % M;
                tmp[i][j] %= M;
            }
        }
    }
    for (int i = 0; i < 4; i++) x[i / 2][i % 2] = tmp[i / 2][i % 2];
}
int main()
{
    scanf("%lld", &n);
    while (n)
    {
        if (n & 1)
            pow(ans, m);
        pow(m, m);
        n >>= 1;
    }
    printf("%lld", ans[0][1]);
    return 0;
}