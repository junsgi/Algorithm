#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
using namespace std;
int n, arr[200000], st, ed, ck[11], ans = 1;
int cnt()
{
    int res = 0;
    for (int i = 1; i <= 9; i++)
        if (ck[i]) res++;
    return res;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    ck[arr[0]] = 1;
    while (st <= ed && ed < n)
    {
        if (ed < n && cnt() <= 2)
        {
            ed++;
            if (ed < n)
                ck[arr[ed]]++;
        }
        else if (cnt() > 2)
        {
            int element = arr[st];
            while (st < n && element == arr[st])
            {
                ck[element]--;
                st++;
            }
        }
        if (ed < n && cnt() <= 2) ans = max(ans, ed - st + 1);
    }
    cout << ans;
    return 0;
}