#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
using namespace std;
int n, a, b = 9999999, matrix[100000][3], x[2][3], y[2][3];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> matrix[i][0] >> matrix[i][1] >> matrix[i][2];
    if (n == 1)
    {
        cout << max(matrix[0][0], max(matrix[0][1], matrix[0][2])) << " " << min(matrix[0][0], min(matrix[0][1], matrix[0][2]));
        return 0;
            
    }
    for (int i = 0 ; i < 2; i++)
    {
        x[i][0] = y[i][0] = matrix[n - 2 + i][0];
        x[i][1] = y[i][1] = matrix[n - 2 + i][1];
        x[i][2] = y[i][2] = matrix[n - 2 + i][2];
    }
    for (int i = n - 2; i >= 0; i--)
    {
        x[0][0] += max(x[1][0], x[1][1]);
        x[0][1] += max(x[1][0], max(x[1][1], x[1][2]));
        x[0][2] += max(x[1][1], x[1][2]);

        y[0][0] += min(y[1][0], y[1][1]);
        y[0][1] += min(y[1][0], min(y[1][1], y[1][2]));
        y[0][2] += min(y[1][1], y[1][2]);

        for (int j = 0; i - 1 >= 0 && j < 3; j++)
        {
            x[1][j] = x[0][j];
            y[1][j] = y[0][j];
            x[0][j] = y[0][j] = matrix[i - 1][j];
        }
    }
    a = max(x[0][0], max(x[0][1], x[0][2]));
    b = min(y[0][0], min(y[0][1], y[0][2]));
    cout << a << " " << b;
    return 0;
}
