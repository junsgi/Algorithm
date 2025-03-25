#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
using namespace std;
struct Temp {
    int node, w;
    bool operator<(const Temp& other) const {
        return w < other.w;
    }
};
int n, m, k;
vector<int> maxHeap[1001];
vector<Temp> heap, graph[1001];
template <typename T>
void up(int idx, vector<T>& heap);
template <typename T>
void down(int idx, vector<T>& heap);
void init()
{
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        graph[a].push_back({ b, c });
    }
    // 최소힙, 최대힙 초기화
    heap = vector<Temp>(1);
    for (int i = 1; i <= n; i++)
        maxHeap[i] = vector<int>(1);
}
void dijkstra()
{
    heap.push_back({ 1, 0 });
    maxHeap[1].push_back(0);
    while (heap.size() != 1)
    {
        int node = heap[1].node;
        int weight = heap[1].w;
        heap[1] = heap.back();heap.pop_back();
        down(1, heap);
        if (maxHeap[node].size() - 1 == k && -maxHeap[node][1] < weight ) continue;
        for (Temp& i : graph[node])
        {
            int tnode = i.node;
            int tw = i.w;
            if (maxHeap[tnode].size() - 1 < k)
            {
                maxHeap[tnode].push_back(-(weight + tw));
                up((int)maxHeap[tnode].size() - 1, maxHeap[tnode]);

                heap.push_back({ tnode, weight + tw });
                up((int)heap.size() - 1, heap);
            }
            else if (-maxHeap[tnode][1] > weight + tw) // 최대값이 현재 가중치보다 크다면 빼고 현재 가중치를 넣는다
            {
                maxHeap[tnode][1] = maxHeap[tnode].back();
                maxHeap[tnode].pop_back();
                down(1, maxHeap[tnode]);

                maxHeap[tnode].push_back(-(weight + tw));
                up((int)maxHeap[tnode].size() - 1, maxHeap[tnode]);

                heap.push_back({ tnode, weight + tw });
                up((int)heap.size() - 1, heap);
            }
        }
    }
}
void answer()
{
    for (int i = 1; i <= n; i++)
    {
        if (maxHeap[i].size() - 1 != k)
            printf("-1\n");
        else
            printf("%d\n", -maxHeap[i][1]);
    }
}
int main()
{
    init();
    dijkstra();
    answer();
    return 0;
}


template <typename T>
void up(int idx, vector<T>& heap)
{
    if (idx / 2 == 0) return;
    if (heap[idx] < heap[idx / 2])
    {
        auto temp = heap[idx];
        heap[idx] = heap[idx / 2];
        heap[idx / 2] = temp;
        up(idx / 2, heap);
    }
}
template <typename T>
void down(int idx, vector<T>& heap)
{
    int child = idx * 2;
    if (child >= heap.size()) return;
    if (child + 1 < heap.size() && heap[child + 1] < heap[child]) child++;
    if (heap[child] < heap[idx])
    {
        auto temp = heap[idx];
        heap[idx] = heap[child];
        heap[child] = temp;
        down(child, heap);
    }

}