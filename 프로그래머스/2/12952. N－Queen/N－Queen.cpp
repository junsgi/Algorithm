#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int col[100], lr[100], rr[100], idx;
int dfs(int row, int n)
{
    if (row == n)
    {
        return 1;
    }
    int result = 0;
    for(int i = 0 ; i < n ; i++)
    {
        if (col[i] + lr[row - i + n] + rr[row + i]) continue;
        col[i] = lr[row - i + n] = rr[row + i] = 1;
        result += dfs(row + 1, n);
        col[i] = lr[row - i + n] = rr[row + i] = 0;
    }
    return result;
}
int solution(int n) {
    return dfs(0, n);
}