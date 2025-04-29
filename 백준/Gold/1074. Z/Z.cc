#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int n, r, c;
int zip(int x, int y, int len, int depth, int ex)
{
    if (len == 1)
    {
        if (x == r && y == c) return depth;
        else if (x == r && y + 1 == c) return depth + 1;
        else if (x + 1 == r && y == c) return depth + 2;
        else return depth + 3;
    }
    int tlen = len / 2;
    int x1 = x, y1 = y + tlen;
    int x2 = x, y2 = y;
    int x3 = x + tlen, y3 = y;
    int x4 = x + tlen, y4 = y + tlen;
    int tdepth = 1 << ex;
    tdepth *= tdepth;
    if (tdepth == 0) tdepth++;
    if (x1 <= r && r < x1 + tlen && y1 <= c && c < y1 + tlen)
        return zip(x1, y1, tlen, depth + tdepth, ex - 1);
    else if (x2 <= r && r < x2 + tlen && y2 <= c && c < y2 + tlen)
        return zip(x2, y2, tlen, depth, ex - 1);
    else if (x3 <= r && r < x3 + tlen && y3 <= c && c < y3 + tlen)
        return zip(x3, y3, tlen, depth + tdepth * 2, ex - 1);
    else if(x4 <= r && r < x4 + tlen && y4 <= c && c < y4 + tlen)
        return zip(x4, y4, tlen, depth + tdepth * 3, ex - 1);
    return 1;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> r >> c;
    cout << zip(0, 0, 1 << n, 0, n - 1);
    return 0;
}