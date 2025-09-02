#include<iostream>
using namespace std;
int ax1, ay1, ax2, ay2, bx1, by1, bx2, by2;
int ccw(int a, int b, int c, int d, int e, int f)
{
    int res = (a * d + c * f + e * b) - (c * b + e * d + a * f);
    if (res > 0) return 1;
    else if (res < 0) return -1;
    return 0;
}
int main()
{
    cin >> ax1 >> ay1 >> ax2 >> ay2 >> bx1 >> by1 >> bx2 >> by2;
    int case1 = ccw(ax1, ay1, ax2, ay2, bx1, by1) * ccw(ax1, ay1, ax2, ay2, bx2, by2);
    int case2 = ccw(bx1, by1, bx2, by2, ax1, ay1) * ccw(bx1, by1, bx2, by2, ax2, ay2);
    if (case1 < 0 && case2 < 0) cout << 1;
    else cout << 0;
    return 0;
}