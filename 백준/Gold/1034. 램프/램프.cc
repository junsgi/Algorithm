#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
int n, m, k, ans;
string s;
unordered_map<string, pair<int, int>> map;
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        ++map[s].first;
        if (map[s].second == 0)
        {
            for (int j = 0; j < m; j++)
                if (s[j] == '0')
                    ++map[s].second;
        }
    }
    cin >> k;
    for (const auto& [_, b] : map)
    {
        const auto& [first, second] = b;
        if (second <= k && (second & 1) == (k & 1))
            ans = max(ans, first);
    }
    cout << ans;
    return 0;
}
