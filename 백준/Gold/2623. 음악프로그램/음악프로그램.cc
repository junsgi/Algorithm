#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int n, m, t, k, before, visit[1001], que[1011], front, rear;
vector<int> graph[1001], ans;
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &t);
        for (int j = 0 ; j < t ; j++)
        {
            scanf("%d", &k);
            if (j > 0)
            {
                visit[k]++;
                graph[before].push_back(k);
            }
            before = k;
        }
    }
    front = rear = -1;
    for (int i = 1; i <= n; i++)
    {
        if (visit[i] != 0) continue;
        que[++rear] = i;
    }
    while (front != rear)
    {
        int node = que[++front];
        ans.push_back(node);
        for (int& tnode : graph[node])
        {
            if (--visit[tnode] == 0)
                que[++rear] = tnode;
        }
    }
    if (ans.size() != n)printf("0");
    else
    {
        for (int& i : ans)
            printf("%d\n", i);
    }
    
    return 0;
}