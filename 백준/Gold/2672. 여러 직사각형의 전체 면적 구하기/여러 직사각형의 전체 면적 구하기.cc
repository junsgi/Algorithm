#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
int n;
double sx[30], sy[30], ex[30], ey[30], ans;
vector<double> x, y;
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%lf%lf%lf%lf", &sx[i], &sy[i], &ex[i], &ey[i]);
        ex[i] += sx[i]; ey[i] += sy[i];
        x.emplace_back(sx[i]); x.emplace_back(ex[i]);
        y.emplace_back(sy[i]); y.emplace_back(ey[i]);
    }
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    for (int i = 1; i < x.size(); i++)
    {
        if (x[i - 1] == x[i]) continue;
        for (int j = 1; j < y.size(); j++)
        {
            if (y[j - 1] == y[j]) continue;
            int flag = 0;
            for (int k = 0; k < n; k++)
            {
                if (sx[k] <= x[i - 1] && x[i] <= ex[k] && sy[k] <= y[j - 1] && y[j] <= ey[k])
                {
                    flag = 1;
                    break;
                }
            }
            if (flag) ans += (x[i] - x[i - 1]) * (y[j] - y[j - 1]);
        }
    }
    if (floor(ans) == ans) printf("%lld", (long long)floor(ans));
    else
        printf("%.2lf", ans);
    return 0;
}