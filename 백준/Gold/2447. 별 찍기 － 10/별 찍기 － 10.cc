#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
using namespace std;
int n;
char ans[2187][2187];
void star(int x, int y, int len, int no)
{
    if (len == 1)
    {
        if (no != 4) ans[x][y] = '*';
        else ans[x][y] = ' ';
        return;
    }
    int p = len / 3;
    for (int i = 0; i < 9; i++)
        star(x + (i / 3) * p, y + (i % 3) * p, len / 3, no == 4 ? 4 : i);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    star(0, 0, n, 0);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << ans[i][j];
        cout << '\n';
    }
    return 0;
}
