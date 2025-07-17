#pragma warning(disable:4996)
#include <iostream>
using namespace std;
int n, arr[13], visit[13];
void p(int depth, int s)
{
    if (depth == n)
    {
        if (s != 6) return;
        for (int i = 0; i < n; i++)
        {
            if (!visit[i]) continue;
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }

    visit[depth] = 1;
    p(depth + 1, s + 1);
    visit[depth] = 0;

    p(depth + 1, s);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    while (1)
    {
        cin >> n;
        if (!n) break;
        for (int i = 0; i < n; i++) cin >> arr[i];
        p(0, 0);
        cout << '\n';
    }
    return 0;
}
