#include <vector>
#include <iostream>
using namespace std;
struct Temp{
    int prev, node, index, error;
};
int visit[201][201][101], len;
Temp heap[201 * 201 * 101];
vector<int> graph[201];
void up(int idx);
void down(int idx);
int dijkstra(vector<int>& log, int k)
{
    len = 0;
    heap[++len] = {0, log[0], 1, 0};
    visit[0][log[0]][1] = 0;
    while(len)
    {
        Temp tmp = heap[1];
        heap[1] = heap[len--];
        down(1);
        int node = tmp.node;
        int depth = tmp.error;
        if (visit[tmp.prev][tmp.node][tmp.index] < depth) continue;
        for(int i = 0 ; i < graph[node].size(); i++)
        {
            int tnode = graph[node][i];
            if(tnode == log[k - 1] && tmp.index == k - 1)
                return depth;
            if (tmp.index == k - 1 && tnode != log[k - 1])
                continue;
            if (tnode == log[tmp.index] && depth < visit[node][tnode][tmp.index + 1])
            {
                visit[node][tnode][tmp.index + 1] = depth;
                heap[++len] = {node, tnode, tmp.index + 1, depth};
                up(len);
            }
            else if (tnode != log[tmp.index] && depth + 1 < visit[node][tnode][tmp.index])
            {
                visit[node][tnode][tmp.index] = depth + 1;
                heap[++len] = {node, tnode, tmp.index + 1, depth + 1};
                up(len);
            }
        }
    }
    return -1;
}

void up(int idx)
{
    if (idx / 2 <= 0) return;
    if (heap[idx].error < heap[idx / 2].error)
    {
        Temp tmp = heap[idx]; heap[idx] = heap[idx / 2]; heap[idx / 2] = tmp;
        up(idx / 2);
    }
}
void down(int idx)
{
    int child = idx * 2;
    if (child > len) return;
    if (child + 1 <= len && heap[child].error > heap[child + 1].error)
        child++;
    if (heap[idx].error > heap[child].error)
    {
        Temp tmp = heap[idx]; heap[idx] = heap[child]; heap[child] = tmp;
        down(child);
    }
}
int solution(int n, int m, vector<vector<int>> edge_list, int k, vector<int> gps_log) {
    int answer = 0;
    int MAX = 0x7fffffff;
    for(int i = 0 ; i < 201 ; i++)
        for(int j = 0 ; j < 201 ; j++)
            for(int k = 0 ; k < 101 ; k++)
                visit[i][j][k] = MAX;
    
    for(int i = 0 ; i < 201 ; i++)
    {
        graph[i].clear();
        graph[i].push_back(i);
    }
    for(auto& i : edge_list)
    {
        graph[i[0]].push_back(i[1]);
        graph[i[1]].push_back(i[0]);
    }
    return dijkstra(gps_log, k);
}