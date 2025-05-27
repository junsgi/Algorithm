#pragma warning(disable:4996)
#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;
int n, m;
unordered_map<string, string> map;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    while (n--)
    {
        string a, b;
        cin >> a >> b;
        map.insert(make_pair(a, b));
    }
    while (m--)
    {
        string a;
        cin >> a;
        cout << map[a] + '\n';
    }
    return 0;
}
