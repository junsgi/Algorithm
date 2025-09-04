#include<iostream>
using namespace std;
using ll = long long;
ll ax1, ay1, ax2, ay2, bx1, by1, bx2, by2;
ll ccw(ll a, ll b, ll c, ll d, ll e, ll f)
{
    ll res = (a * d + c * f + e * b) - (c * b + e * d + a * f);
    if (res > 0) return 1;
    else if (res < 0) return -1;
    return 0;
}
int main()
{
    cin >> ax1 >> ay1 >> ax2 >> ay2 >> bx1 >> by1 >> bx2 >> by2;
    ll case1 = ccw(ax1, ay1, ax2, ay2, bx1, by1) * ccw(ax1, ay1, ax2, ay2, bx2, by2);
    ll case2 = ccw(bx1, by1, bx2, by2, ax1, ay1) * ccw(bx1, by1, bx2, by2, ax2, ay2);
    if (case1 == 0 && case2 == 0)
        cout << (min(ax1, ax2) <= max(bx1, bx2) && min(bx1, bx2) <= max(ax1, ax2) && min(ay1, ay2) <= max(by1, by2) && min(by1, by2) <= max(ay1, ay2));
    else if (case1 <= 0 && case2 <= 0) cout << 1;
    else cout << 0;
    return 0;
}