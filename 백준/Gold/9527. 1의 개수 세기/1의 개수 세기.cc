#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#define MAX 55
using namespace std;
using ll = long long;
ll a, b, p[MAX];
ll pro(ll x)
{
    ll ans = x & 1;
    for (ll i = MAX - 1; i > 0; i--)
    {
        if (x & (1ll << i))
        {
            ans += p[i - 1] + (x - (1ll << i) + 1);
            x -= (1ll << i);
        }
    }
    return ans;
}
int bit(int x)
{
    return x ? bit(x / 2) * 10 + x % 2 : 0;
}
int main()
{
    p[0] = 1;
    for (int i = 1; i < MAX; i++)
        p[i] = p[i - 1] * 2 + (1ll << i);
    scanf("%lld%lld", &a, &b);
    printf("%lld", pro(b) - pro(a - 1));
    return 0;
}
/*
1bit : 1
2bit : 4
3bit : 12

 00
 01
 10
 11
100
101
110
111
3개 비트일 때 (2비트 1의 개수 * 2) + 최상 위치의 1의 개수(즉 2 ^ i - 1)

x개 이하의 비트를 사용할 때, 1의 총 개수는
sum[x] = sum[x - 1] * 2 + (1 << i)

101101(2)가 있을 때
101101 & (1 << 5)는 0이 아니므로 sum[5 - 1]과 101101 - (1 << 5) + 1를 더해준다
최상 비트를 빼고 1을 더해주는 이유는 최상 비트 1과 나머지는 0으로만 이루어진 경우이다.

if x & (1 << i):
    ans += sum[i - 1] + (x - (1 << i) + 1)
계산 후 최상단 비트는 뺀다
x -= 1 << i
*/