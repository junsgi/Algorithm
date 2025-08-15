#include <iostream>
#include <unordered_set>
#include <queue>
#include <string>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
struct Node { int arr[3]; Node(int x, int y, int z) : arr{ x, y, z } {} };
int a, b, c;
unordered_set<string> check;
queue<Node> que;
string toString(int x, int y, int z) 
{
    int tmp[] = { z, y, x };
    string res = "";
    for (int& i : tmp)
        while (i) { res = string(1, (i % 10 + '0')) + res; i /= 10; }
    return res;
}
int main()
{
    fastio;
    cin >> a >> b >> c;
    que.emplace(Node(a, b, c));
    check.insert(toString(a, b, c));
    while (!que.empty())
    {
        auto [arr] = que.front();
        que.pop();
        if (arr[0] == arr[1] && arr[1] == arr[2])
        {
            cout << 1;
            return 0;
        }
        for (int i = 0; i < 2; i++)
        {
            for (int j = 1; j < 3; j++)
            {
                if (arr[i] == arr[j]) continue;
                int origini = arr[i], originj = arr[j];
                int x = arr[i], y = arr[j];
                if (x < y)
                {
                    y -= x;
                    x += x;
                }
                else
                {
                    x -= y;
                    y += y;
                }
                arr[i] = x;
                arr[j] = y;
                string ck = toString(arr[0], arr[1], arr[2]);
                if (check.find(ck) == check.end())
                {
                    que.emplace(arr[0], arr[1], arr[2]);
                    check.insert(ck);
                }
                arr[i] = origini;
                arr[j] = originj;
            }
        }
    }
    cout << 0;
    return 0;
}