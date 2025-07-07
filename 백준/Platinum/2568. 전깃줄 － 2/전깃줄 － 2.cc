#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
using pii = pair<int, int>;
int n, trace[100000], idx;
vector<pii> arr;
vector<int> sequence, ans;
int main()
{
    scanf("%d", &n);
    arr.resize(n);
    for (pii& i : arr)
        scanf("%d%d", &i.first, &i.second);
    sort(arr.begin(), arr.end());
    for (int i = 0 ; i < n ; i++)
    {
        auto& [x, y] = arr[i];
        if (sequence.empty() || sequence.back() <= y)
        {
            trace[i] = idx++;
            sequence.push_back(y);
        }
        else
        {
            int res = lower_bound(sequence.begin(), sequence.end(), y) - sequence.begin();
            trace[i] = res;
            sequence[res] = y;
        }
    }
    printf("%d\n", n - (int)sequence.size());

    for (int i = n - 1; i >= 0; i--)
    {
        if (trace[i] + 1 == idx)idx--;
        else ans.push_back(arr[i].first);
    }
    for (int i = ans.size() - 1; i >= 0; i--)
        printf("%d\n", ans[i]);
    return 0;
}