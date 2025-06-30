#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;
int n;
ll tmp, MIN = 1ll << 32, a, b, c;
vector<ll> arr;
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", &tmp);
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end());
    for (int i = 0; i < n - 2; i++)
    {
        int x = i + 1, y = n - 1;
        ll min = 1ll << 32;
        while (x < y)
        {
            tmp = arr[i] + arr[x] + arr[y];
            if (abs(tmp) < MIN)
            {
                MIN = abs(tmp);
                a = arr[i]; b = arr[x]; c = arr[y];
            }
            if (tmp < 0) x++;
            else y--;
        }
    }
    printf("%lld %lld %lld", a, b, c);
    return 0;
}