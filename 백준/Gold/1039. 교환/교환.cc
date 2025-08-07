#include <iostream>
#include <queue>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int n, k, cnt, visit[11][1'000'001], tmp, ans;
queue<pair<int*, int>> que;
int getNum(int* arr)
{
    int res = 0;
    for (int i = 0; i < cnt; i++)
        res = res * 10 + arr[i];
    return res;
}
void init()
{
    fastio;
    cin >> n >> k;
    int m = n;
    while (m) { ++cnt; m /= 10; }

    int* num = new int[cnt];
    m = n;
    visit[0][m] = 1;
    for (int i = cnt - 1; i >= 0; --i)
    {
        num[i] = m % 10;
        m /= 10;
    }
    que.emplace(num, 0);
}
int* _swap(int a, int b, int* arr)
{
    int* res = new int[cnt];
    for (int i = 0; i < cnt; i++) res[i] = arr[i];
    tmp = res[a]; res[a] = res[b]; res[b] = tmp;
    return res;
}
void solution()
{
    while (!que.empty())
    {
        auto& [arr, depth] = que.front();
        if (depth == k)
        {
            ans = max(ans, getNum(arr));
            delete[] arr;
            que.pop();
            continue;
        }
        for (int i = 0; i < cnt - 1; i++)
        {
            for (int j = i + 1; j < cnt; j++)
            {
                int* res = _swap(i, j, arr);
                if (res[0] == 0 || visit[depth + 1][getNum(res)]) continue;
                visit[depth + 1][getNum(res)] = 1;
                que.emplace(res, depth + 1);
            }
        }

        delete[] arr;
        que.pop();
    }
    if (!ans) cout << -1;
    else cout << ans;
}
int main()
{
    init();
    solution();
    return 0;
}