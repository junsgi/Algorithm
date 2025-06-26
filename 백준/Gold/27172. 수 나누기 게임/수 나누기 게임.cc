#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, arr[100000], ans[1'000'001], check[1'000'001];
void pro(int num)
{
    for (int i = num * 2; i <= 1'000'000; i += num)
    {
        if (check[i])
        {
            ans[num]++;
            ans[i]--;
        }
    }
}
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        check[arr[i]] = 1;
    }
    for (int i = 0; i < n; i++)
        pro(arr[i]);
    for (int i = 0; i < n; i++)
        printf("%d ", ans[arr[i]]);
    return 0;  
}