#include<iostream>
#include<algorithm>
#include<stack>
using namespace std;
int n, arr[500'001], ans[500'001];
stack<pair<int, int>> stk;
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n;
    for (int i = 1; i <= n; ++i) 
        cin >> arr[i];
    for (int i = 1; i <= n; ++i)
    {
        if (stk.empty() || stk.top().first > arr[i]) stk.emplace(arr[i], i);
        else
        {
            while (!stk.empty() && stk.top().first <= arr[i])
            {
                auto [node, idx] = stk.top(); stk.pop();
                if (stk.empty())
                    ans[idx] = 0;
                else
                    ans[idx] = stk.top().second;
            }
            stk.emplace(arr[i], i);
        }
    }
    while (!stk.empty())
    {
        auto [node, idx] = stk.top(); stk.pop();
        if (stk.empty())
            ans[idx] = 0;
        else
            ans[idx] = stk.top().second;
    }
    for (int i = 1; i <= n; ++i)
        cout << ans[i] << ' ';
    return 0;
}