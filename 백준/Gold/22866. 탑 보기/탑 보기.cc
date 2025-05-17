#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<stack>
using namespace std;
struct Node { int node, idx;  Node(int a, int b) : node(a), idx(b) {} };
int n, arr[100000], cnt[100000], ans[100000], dist[100000];
stack<Node> left, right;
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        dist[i] = 9999999;
    }
    for (int i = 0; i < n; i++) // 왼쪽에 있는 건물
    {
        // 현재 건물 높이 이하의 건물은 모두 뺀다.
        while (!left.empty() && arr[i] >= left.top().node) left.pop();
        cnt[i] += left.size();
        if (!left.empty() && (dist[i] > i - left.top().idx || dist[i] == i - left.top().idx && ans[i] > left.top().idx + 1))
        {
            dist[i] = i - left.top().idx;
            ans[i] = left.top().idx + 1;
        }
        left.emplace(arr[i], i);

        while (!right.empty() && arr[n - i - 1] >= right.top().node) right.pop();
        cnt[n - i - 1] += right.size();
        if (!right.empty() && (dist[n - i - 1] > right.top().idx - (n - i - 1) || dist[n - i - 1] == right.top().idx - (n - i - 1) && ans[n - i - 1] > right.top().idx + 1))
        {
            dist[n - i - 1] = right.top().idx - (n - i - 1);
            ans[n - i - 1] = right.top().idx + 1;
        }
        right.emplace(arr[n - i - 1], n - i - 1);
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d", cnt[i]);
        if (cnt[i]) printf(" %d", ans[i]);
        printf("\n");
    }
    return 0;
}
