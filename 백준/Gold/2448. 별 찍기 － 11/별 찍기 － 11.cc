#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
using namespace std;
int n, ck[11];
char ans[6144][6145], p[5][6] = { "  *  ", " * * ", "*****"};
void star(int x, int y, int no)
{
    if (no == 0)
    {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 5; j++)
                ans[x + i][y - 2 + j] = p[i][j];
        return;
    }
    int tlen = ck[no - 1];
    star(x, y, no - 1);
    star(x + tlen, y - tlen, no - 1);
    star(x + tlen, y + tlen, no - 1);

}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    int t = 1, loc = -1;
    for (int i = 0; i < 11; i++)
    {
        ck[i] = t * 3;
        t *= 2;
        if (ck[i] == n) loc = i;
    }
    for (int i = 0; i < (n * 2) * (n * 2); i++) ans[i / (n * 2)][i % (n * 2)] = ' ';

    star(0, n - 1, loc);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n * 2; j++)
            cout << ans[i][j];
        if (i != n - 1)
            cout << '\n';
    }
    return 0;
}
