#include<stdio.h>
#include<vector>
using namespace std;
int n, m, check[32'001], tmp;
vector<int> graph[32'001], heap;
void up(int idx);
void down(int idx);
int main()
{
    scanf("%d%d", &n, &m);
    heap.push_back(-1);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        check[b]++;
        graph[a].push_back(b);
    }
    for (int i = 1; i <= n; i++)
    {
        if (check[i]) continue;
        heap.push_back(i);
        up(heap.size() - 1);
    }
    while (heap.size() != 1)
    {
        int node = heap[1];
        printf("%d ", node);
        heap[1] = heap.back();
        heap.pop_back();
        down(1);
        for (int& tnode : graph[node])
        {
            if (check[tnode] == 1)
            {
                check[tnode] = 0;
                heap.push_back(tnode);
                up(heap.size() - 1);
            }
            else if (check[tnode] > 1)
                check[tnode]--;
        }
    }
    return 0;
}
void up(int idx)
{
    if (idx / 2 <= 0) return;
    if (heap[idx] < heap[idx / 2])
    {
        tmp = heap[idx];
        heap[idx] = heap[idx / 2];
        heap[idx / 2] = tmp;
        up(idx / 2);
    }
}
void down(int idx)
{
    int child = idx * 2;
    if (child >= heap.size()) return;
    if (child + 1 < heap.size() && heap[child] > heap[child + 1]) child++;
    if (heap[idx] > heap[child])
    {
        tmp = heap[idx];
        heap[idx] = heap[child];
        heap[child] = tmp;
        down(child);
    }
}
