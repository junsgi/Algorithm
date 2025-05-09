#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#define M 50000000000ll
using namespace std;
int n, m, hit, x[6000], y[6000];
long long cost[501], z[6000];
int main()
{
    scanf("%d%d", &n, &m);
    fill(cost + 1, cost + n + 1, M);
    for (int i = 0; i < m; i++)
        scanf("%d%d%lld", &x[i], &y[i], &z[i]);
    cost[1] = 0;
    for (int i = 0; i < n; i++)
    {
        hit = 0;
        for (int j = 0; j < m; j++)
        {
            if (cost[x[j]] == M) continue;
            if (cost[y[j]] <= cost[x[j]] + z[j]) continue;
            hit = 1;
            cost[y[j]] = cost[x[j]] + z[j];
        }
    }
    if (hit) printf("-1");
    else
        for (int i = 2; i <= n; i++)
            printf("%lld\n", cost[i] == M ? -1 : cost[i]);
    return 0;
}
