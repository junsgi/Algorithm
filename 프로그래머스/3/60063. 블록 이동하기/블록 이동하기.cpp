#include <stdio.h>
#include <vector>
using namespace std;
struct temp {
    int x, y, z;
};
int visit[4][100][100], dire[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
int front = -1, rear = -1, path[4 * 100 * 100 + 1];
temp Q[4 * 100 * 100 + 1];
int inRange(int x, int y, int N, int M)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
vector<temp> get(temp& a, int N, int M, vector<vector<int>>& graph)
{
    vector<temp> res;
    int x1 = a.x;
    int y1 = a.y;
    int z = a.z;
    int x2 = x1 + dire[z][0];
    int y2 = y1 + dire[z][1];
    int depth = visit[z][x1][y1];
    for (int i = 0; i < 4; i++)
    {
        int t1x = x1 + dire[i][0];
        int t1y = y1 + dire[i][1];
        int t2x = x2 + dire[i][0];
        int t2y = y2 + dire[i][1];
        if (inRange(t1x, t1y, N, M) && inRange(t2x, t2y, N, M) && graph[t1x][t1y] + graph[t2x][t2y] == 0 && visit[z][t1x][t1y] == 0)
        {
            res.push_back({ t1x, t1y, z });
            visit[z][t1x][t1y] = depth + 1;
        }
    }
    int tx, ty;
    if (z == 0) // (x1,y1 기준) 오른쪽 위 또는 오른쪽 아래, (x2, y2) 기준 왼쪽 위 또는 왼쪽 아래
    {
        tx = x1 - 1; ty = y1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx][ty + 1] == 0 && visit[3][x1][y1] == 0)
        {
            visit[3][x1][y1] = depth + 1;
            res.push_back({ x1, y1, 3 });
        }
        tx = x1 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx][ty + 1] == 0 && visit[1][x1][y1] == 0)
        {
            visit[1][x1][y1] = depth + 1;
            res.push_back({ x1, y1, 1 });
        }

        tx = x2 - 1; ty = y2;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx][ty - 1] == 0 && visit[3][x2][y2] == 0)
        {
            visit[3][x2][y2] = depth + 1;
            res.push_back({ x2, y2, 3 });
        }
        tx = x2 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx][ty - 1] == 0 && visit[1][x2][y2] == 0)
        {
            visit[1][x2][y2] = depth + 1;
            res.push_back({ x2, y2 , 1 });
        }

    }
    else if (z == 1) // (x1, y1) 기준 왼쪽 아래 또는 오른쪽 아래, (x2, y2)기준 왼쪽 위 또는 오른쪽 위
    {
        tx = x1; ty = y1 - 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx + 1][ty] == 0 && visit[2][x1][y1] == 0)
        {
            visit[2][x1][y1] = depth + 1;
            res.push_back({ x1, y1, 2 });
        }
        ty = y1 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx + 1][ty] == 0 && visit[0][x1][y1] == 0)
        {
            visit[0][x1][y1] = depth + 1;
            res.push_back({ x1, y1, 0 });
        }

        tx = x2; ty = y2 - 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx - 1][ty] == 0 && visit[2][x2][y2] == 0)
        {
            visit[2][x2][y2] = depth + 1;
            res.push_back({ x2, y2, 2 });
        }
        ty = y2 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx - 1][ty] == 0 && visit[0][x2][y2] == 0)
        {
            visit[0][x2][y2] = depth + 1;
            res.push_back({ x2, y2, 0 });
        }
    }
    else if (z == 2) // (x1, y1) 기준 왼쪽 위 또는 왼쪽 아래, (x2, y2) 기준 오른쪽 위 또는 오른쪽 아래
    {
        tx = x1 - 1; ty = y1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx][ty - 1] == 0 && visit[3][x1][y1] == 0)
        {
            visit[3][x1][y1] = depth + 1;
            res.push_back({ x1, y1, 3 });
        }
        tx = x1 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx][ty - 1] == 0 && visit[1][x1][y1] == 0)
        {
            visit[1][x1][y1] = depth + 1;
            res.push_back({ x1, y1 , 1 });
        }

        tx = x2 - 1; ty = y2;
        if (inRange(tx, ty, N, M) &&graph[tx][ty] + graph[tx][ty + 1] == 0 && visit[3][x2][y2] == 0)
        {
            visit[3][x2][y2] = depth + 1;
            res.push_back({ x2, y2, 3 });
        }
        tx = x2 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx][ty + 1] == 0 && visit[1][x2][y2] == 0)
        {
            visit[1][x2][y2] = depth + 1;
            res.push_back({ x2, y2, 1 });
        }

    }
    else if (z == 3) // (x1, y1) 기준 왼쪽 위 또는 오른쪽 위, (x2, y2) 기준 왼쪽 아래 또는 오른쪽 아래
    {
        tx = x1; ty = y1 - 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx - 1][ty] == 0 && visit[2][x1][y1] == 0)
        {
            visit[2][x1][y1] = depth + 1;
            res.push_back({ x1, y1, 2 });
        }
        ty = y1 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx - 1][ty] == 0 && visit[0][x1][y1] == 0)
        {
            visit[0][x1][y1] = depth + 1;
            res.push_back({ x1, y1, 0 });
        }

        tx = x2; ty = y2 - 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx + 1][ty] == 0 && visit[2][x2][y2] == 0)
        {
            visit[2][x2][y2] = depth + 1;
            res.push_back({ x2, y2, 2 });
        }
        ty = y2 + 1;
        if (inRange(tx, ty, N, M) && graph[tx][ty] + graph[tx + 1][ty] == 0 && visit[0][x2][y2] == 0)
        {
            visit[0][x2][y2] = depth + 1;
            res.push_back({ x2, y2, 0 });
        }
    }
    return res;
}

void traceback(int node, int depth)
{
    if (path[node] == -1)
    {
        printf("(0, 0), (0, 1), z = 0\n");
        return;
    }
    traceback(path[node], depth - 1);
    printf("(%d, %d), (%d, %d), z = %d\n", Q[node].x, Q[node].y, Q[node].x + dire[Q[node].z][0], Q[node].y + dire[Q[node].z][1], Q[node].z);
    return;
}

int BFS(vector<vector<int>>& graph)
{
    int N = graph.size();
    int M = graph[0].size();
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k < M; k++)
                visit[i][j][k] = 0;
    Q[++rear] = { 0, 0, 0 };
    path[0] = -1;
    visit[0][0][0] = 1;
    while (front != rear)
    {
        temp node = Q[++front];
        vector<temp> list = get(node, N, M, graph);
        for (int i = 0; i < list.size(); i++)
        {
            if ((list[i].x == N - 1 && list[i].y == M - 1) || (list[i].x + dire[list[i].z][0] == N - 1 && list[i].y + dire[list[i].z][1] == M - 1))
            {
                // 역추적
                //traceback(front, visit[list[i].z][list[i].x][list[i].y] - 1);
                return visit[list[i].z][list[i].x][list[i].y] - 1;
            }
            Q[++rear] = list[i];
            path[rear] = front;

        }

    }
}
int solution(vector<vector<int>> board) {
    int answer = 0;
    return BFS(board);
}