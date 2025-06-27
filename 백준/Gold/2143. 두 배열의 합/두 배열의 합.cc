#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int n, m, tmp;
long long ans, t;
vector<int> a{ 0 }, b{ 0 }, sa, sb;
void input()
{
    scanf("%lld%d", &t, &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        a.push_back(tmp + a[i]);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &tmp);
        b.push_back(tmp + b[i]);
    }
    for (int i = 1; i <= n; i++)
        for (int j = i; j <= n; j++)
            sa.push_back(a[j] - a[i - 1]);

    for (int i = 1; i <= m; i++)
        for (int j = i; j <= m; j++)
            sb.push_back(b[j] - b[i - 1]);

}
void solution()
{
    sort(sb.begin(), sb.end());
    for (const long long& num : sa)
    {
        int upper = upper_bound(sb.begin(), sb.end(), t - num) - sb.begin();
        int lower = lower_bound(sb.begin(), sb.end(), t - num) - sb.begin();
        ans += upper - lower;
    }
    printf("%lld", ans);
}
int main()
{
    input();
    solution();
    return 0;
}
/*
부배열
 - 누적합 배열을 만든다
 - 반복문으로 i~j 합을 모두 구한다.
 - i ~ j는 연속됨이 보장됨 ex) 1, 2, 3(O)   1, 4, 5 (X)
*/