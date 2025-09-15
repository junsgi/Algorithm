#include<iostream>
using namespace std;
int n, m, a[100];
int main()
{
    cin >> n >> m;
    for(int i = 0 ; i < n ; ++i) a[i] = i + 1;
    while(m--)
    {
        int x, y;
        cin >> x >> y;--x;--y;
        swap(a[x], a[y]);
    }
    for(int i = 0 ; i < n ; ++i)
        cout << a[i] << ' ';
    return 0;
}