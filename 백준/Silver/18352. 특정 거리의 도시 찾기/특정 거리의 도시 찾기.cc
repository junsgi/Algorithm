#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int n, m, k, s, cost[300001];
struct Node 
{
    int node, weight; 
    Node(int a, int b) : node(a), weight(b) {};
    bool operator>(const Node& other) const {
        return weight > other.weight;  // '>'를 써야 최소 힙처럼 동작함
    }
};
vector<int> graph[300001];
priority_queue<Node, vector<Node>, greater<Node>> heap;
int main()
{
    scanf("%d%d%d%d", &n, &m, &k, &s);
    fill(cost, cost + n + 1, 100000000);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        graph[a].push_back(b);
    }
    heap.emplace(s, 0);
    cost[s] = 0;
    while (!heap.empty())
    {
        Node t = heap.top(); heap.pop();
        int node = t.node;
        int weight = t.weight;
        if (cost[node] < weight) continue;
        for (const int& tnode : graph[node])
        {
            if (cost[tnode] <= cost[node] + 1) continue;
            cost[tnode] = cost[node] + 1;
            heap.emplace(tnode, cost[tnode]);
        }
    }
    int hit = 0;
    for (int i = 1; i <= n; i++)
    {
        if (cost[i] == k)
        {
            printf("%d\n", i);
            hit = 1;
        }

    }
    if (!hit) printf("-1");
    return 0;
}
