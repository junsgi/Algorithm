#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
using pii = pair<int, int>;
int n, d, st, ed, s, ans;
vector<pii> arr;
priority_queue<int, vector<int>, greater<int>> heap;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        if (a < b) arr.emplace_back(a, b);
        else arr.emplace_back(b, a);
    }
    // 도착지를 기준으로 정렬
    sort(arr.begin(), arr.end(), [&](pii& x, pii& y) { return x.second < y.second || (x.second == y.second && x.first < y.first); });
    cin >> d;

    for (auto& [x, y] : arr)
    {
        if (y - x <= d) heap.push(x); // 철로 길이 안에 포함된다면 heap에 추가
        else continue;
        while (!heap.empty() && y - heap.top() > d) // 철로 길이보다 넘어서면 pop
            heap.pop();
        ans = max((int)heap.size(), ans);
    }
    cout << ans;
    return 0;
}