#pragma warning(disable:4996)
#include<stdio.h>
int n, m, inven, arr[500 * 500], min = 0x7fffffff, max, ans, ck = 0x7fffffff;
int main()
{
    scanf("%d%d%d", &n, &m, &inven);
    for (int i = 0; i < n * m; i++)
    {
        scanf("%d", &arr[i]);
        min = min < arr[i] ? min : arr[i];
        max = max < arr[i] ? arr[i] : max;
    }
    for (int i = min; i <= max; i++)
    {
        int time = 0, plus = 0, minus = 0;
        for (int j = 0; j < n * m; j++)
        {
            if (arr[j] == i) continue;
            else if (arr[j] < i)
            {
                minus += i - arr[j];
                time += i - arr[j];
            }
            else
            {
                plus += arr[j] - i;
                time += (arr[j] - i) * 2;
            }
        }
        if (inven + plus - minus < 0) continue;
        if (ck >= time)
        {
            ans = i;
            ck = time;
        }
    }
    printf("%d %d", ck, ans);
    return 0;
}