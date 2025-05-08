#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#define M 99999999
using namespace std;
int n, m, graph[100][100];
int main()
{
    scanf("%d%d", &n, &m);
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (i != j) graph[i][j] = M;
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c); a--; b--;
        graph[a][b] = min(graph[a][b], c);
    }
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == j) continue;
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%d ", graph[i][j] == M ? 0 : graph[i][j]);
        printf("\n");
    }
    return 0;
}
