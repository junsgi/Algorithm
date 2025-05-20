#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<queue>
#define M 500'000'000'000LL
using namespace std;
struct Node {
    int node, state;
    long long weight;
    const bool operator<(const Node& x) const {
        return weight > x.weight;
    }
    Node(int a, long long b, int c) : node(a), weight(b), state(c) {}
};
vector<pair<int, int>> graph[100001];
int n, m, a, b;
long long cost[100001];
priority_queue<Node, vector<Node>> heap;
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d%d", &a, &b);
        graph[a].push_back({ b, i });
        graph[b].push_back({ a, i });
    }
    fill(cost + 1, cost + n + 1, M);
    cost[1] = 0;
    heap.emplace(1, 0, 0);
    while (!heap.empty())
    {
        Node con = heap.top(); heap.pop();
        if (cost[con.node] < con.weight) continue;
        for (const pair<int, int>& next : graph[con.node])
        {
            int tcost = 0;
            if (con.state <= next.second)
                tcost = next.second - con.state + 1;
            else
                tcost = m - con.state + next.second + 1;
            
            if (cost[next.first] <= cost[con.node] + tcost) continue;
            cost[next.first] = cost[con.node] + tcost;
            if (next.first == n) continue;
            heap.emplace(next.first, cost[next.first], (next.second + 1) % m);
        }
    }
    printf("%lld", cost[n]);
    return 0;
}
