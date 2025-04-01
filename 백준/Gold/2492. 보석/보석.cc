#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int n, m, t, k, ox[100], oy[100], cnt, ax, ay;
int main()
{
    scanf("%d%d%d%d", &n, &m, &t, &k);
    for (int i = 0; i < t; i++)
        scanf("%d%d", &ox[i], &oy[i]);
    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < t; j++)
        {
            int mx = ox[i] + k, my = oy[j];
            int x = ox[i], y = oy[j] - k;
            int c = 0;
            for (int w = 0; w < t; w++)
                c += (x <= ox[w] && ox[w] <= mx) && (y <= oy[w] && oy[w] <= my);
            if (cnt < c)
            {
                ax = min(ox[i], n - k);
                ay = max(oy[j], k);
                cnt = c;
            }
        }
    }
    printf("%d %d\n%d", ax, ay, cnt);
    return 0;
}
