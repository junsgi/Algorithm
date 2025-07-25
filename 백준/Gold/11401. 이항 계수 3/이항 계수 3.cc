/*
모듈러 연산은 나눗셈에선 분배법칙이 적용되지 않는다.

페르마의 소정리 사용 (e는 소수)
1. n^(e - 1) % e == 1 % e
2. n * n^(e - 2) % e == 1 % e
3. n^(e - 2) % e == n^(-1) % e

즉 (1/n) % e 는 n^(e-2) % e와 같다는 소리

MOD = 1e9+7
nCr = n! / r!(n - r)!
nCr = n! * (r!(n - r)!)^(-1)
nCr = n! * (r!(n - r)!)^(MOD - 2)
nCr = n! % MOD * (r!(n - r)!)^(MOD - 2) % MOD

빠른 거듭제곱이 필요하므로 분할정복을 이용해 logN만에 거듭제곱한다.
*/
#include <iostream>
using namespace std;
using ll = long long;
constexpr ll MOD = 1'000'000'007;
ll n, r, f[4'000'001];
ll power(ll x, ll y)
{
    ll res = 1;
    while (y)
    {
        if (y & 1) res = res * x % MOD;
        x = x * x % MOD;
        y >>= 1;
    }
    return res;
}
ll comb(ll x, ll y)
{
    return (f[x] * power(f[y] * f[x - y] % MOD, MOD - 2) % MOD) % MOD;
}
int main()
{
    cin >> n >> r;
    f[0] = 1;
    for (ll i = 1; i <= n; i++)
        f[i] = f[i - 1] * i % MOD;
    cout << comb(n, r);
    return 0;
}