#pragma warning(disable:4996)
#include<iostream>
#include<string>
#include<unordered_set>
using namespace std;
int n, m, arr[8];
unordered_set<string> set;
int getCnt(int num)
{
    int res = 0;
    while (num) { res++; num /= 10; }
    return res;
}

void nm(int depth, int idx, string print)
{
    if (depth == m)
    {
        if (set.find(print) == set.end())
        {
            set.insert(print);
            cout << print << '\n';
        }
        return;
    }
    for (int i = idx; i < n; i++)
        nm(depth + 1, i, print + to_string(arr[i]) + " ");
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++)
    {
        int idx = i, min = arr[i];
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < min)
            {
                min = arr[j];
                idx = j;
            }
        }
        int tmp = arr[i]; arr[i] = min; arr[idx] = tmp;
    }
    nm(0, 0, "");
    return 0;
}
