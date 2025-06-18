#pragma warning(disable:4996)
#include<iostream>
#include<vector>
using namespace std;
int n, m;
vector<int> a, b, ans;
pair<int, int> max_str_idx(const vector<int>& arr, int x)
{
    int res = 0;
    int idx = -1;
    for (int i = x ; i < (int)arr.size(); i++)
        if (res < arr[i])
        {
            res = arr[i];
            idx = i;
        }
    return {res, idx};
}
void pro(int ax, int bx)
{
    if (ax >= a.size() || bx >= b.size()) return;
    pair<int, int> aMax = max_str_idx(a, ax);
    pair<int, int> bMax = max_str_idx(b, bx);
    if (aMax.first == bMax.first)
    {
        ans.push_back(aMax.first);
        pro(aMax.second + 1, bMax.second + 1);
    }
    else if (aMax.first < bMax.first)
    {
        b.erase(b.begin() + bMax.second);
        pro(ax, bx);
    }
    else
    {
        a.erase(a.begin() + aMax.second);
        pro(ax, bx);
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) { int x; cin >> x; a.push_back(x); }
    cin >> m;
    for (int i = 0; i < m; i++) { int x; cin >> x; b.push_back(x); }
    pro(0, 0);
    cout << ans.size() << '\n';
    for (int& i : ans) cout << i << " ";
    return 0;
}
