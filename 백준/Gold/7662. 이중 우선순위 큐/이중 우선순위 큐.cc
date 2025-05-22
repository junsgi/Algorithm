#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
typedef long long ll;
struct Node
{
    ll node;
    int idx;
    bool operator<(const Node& x) const {
        return node > x.node;
    }
    Node(ll a, int b) : node(a), idx(b) {}
};
ll t, n, tmp;
int ck[1000000];
priority_queue<Node> maxHeap, minHeap;
int main()
{
    scanf("%lld", &t);
    while (t--)
    {
        scanf("%lld", &n);
        maxHeap = priority_queue<Node>();
        minHeap = priority_queue<Node>();
        fill(ck, ck + n, 0);
        for (int i = 0; i < n; i++)
        {
            char a; ll b;
            scanf(" %c%lld", &a, &b);
            if (a == 'I')
            {
                minHeap.emplace(b, i);
                maxHeap.emplace(-b, i);
                ck[i] = 1;
            }
            else if (!minHeap.empty() && b < 0)
            {
                while (!minHeap.empty() && !ck[minHeap.top().idx]) minHeap.pop();
                if (!minHeap.empty())
                {
                    ck[minHeap.top().idx] = 0;
                    minHeap.pop();
                }
            }
            else if (!maxHeap.empty())
            {
                while (!maxHeap.empty() && !ck[maxHeap.top().idx]) maxHeap.pop();
                if (!maxHeap.empty())
                {
                    ck[maxHeap.top().idx] = 0;
                    maxHeap.pop();
                }
            }
        }

        while (!minHeap.empty() && !ck[minHeap.top().idx]) minHeap.pop();
        while (!maxHeap.empty() && !ck[maxHeap.top().idx]) maxHeap.pop();

        if (minHeap.empty() && maxHeap.empty()) printf("EMPTY\n");
        else printf("%lld %lld\n", -maxHeap.top().node, minHeap.top().node);
    }
    return 0;
}
