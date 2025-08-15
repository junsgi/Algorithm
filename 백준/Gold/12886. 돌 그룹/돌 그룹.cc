#include <iostream>
#include <algorithm>
#include <queue>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
struct Node { int arr[3]; Node(int x, int y, int z) : arr{ x, y, z } {} };
int a, b, c, visit[1501][1501];
queue<Node> que;
int main()
{
    fastio;
    cin >> a >> b >> c;
    que.emplace(Node(a, b, c));
    while (!que.empty())
    {
        int* arr = que.front().arr;
        if (arr[0] == arr[1] && arr[1] == arr[2])
        {
            cout << 1;
            return 0;
        }
        sort(arr, arr + 3);
        int tmp[3];
        if (arr[0] != arr[1])
        {
            tmp[0] = arr[0] + arr[0];
            tmp[1] = arr[1] - arr[0];
            tmp[2] = arr[2];
            if (!visit[tmp[0]][tmp[1]])
            {
                visit[tmp[0]][tmp[1]] = 1;
                que.emplace(Node(tmp[0], tmp[1], tmp[2]));
            }
        }
        if (arr[0] != arr[2])
        {
            tmp[0] = arr[0] + arr[0];
            tmp[1] = arr[1];
            tmp[2] = arr[2] - arr[0];
            if (!visit[tmp[0]][tmp[1]])
            {
                visit[tmp[0]][tmp[1]] = 1;
                que.emplace(Node(tmp[0], tmp[1], tmp[2]));
            }
        }
        if (arr[2] != arr[1])
        {
            tmp[0] = arr[0];
            tmp[1] = arr[1] + arr[1];
            tmp[2] = arr[2] - arr[1];
            if (!visit[tmp[0]][tmp[1]])
            {
                visit[tmp[0]][tmp[1]] = 1;
                que.emplace(Node(tmp[0], tmp[1], tmp[2]));
            }
        }
        que.pop();

    }
    cout << 0;
    return 0;
}