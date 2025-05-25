#pragma warning(disable:4996)
#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;
int t, n, cnt, p[30], ans;
string a, b;
map<string, int> check;
int main()
{
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> t;
    while (t--)
    {
        cin >> n;
        cnt = 0;
        ans = 1;
        check.clear();
        fill(p, p + 30, 0);
        while (n--)
        {
            cin >> a >> b;
            if (check.find(b) == check.end())
                check.insert(make_pair(b, cnt++));
            p[check[b]]++;
        }
        for (int i = 0; i < cnt; i++)
            ans *= p[i] + 1;

        cout << ans - 1 << '\n';
    }
    return 0;
}