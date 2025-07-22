/*
첫 시도
1. bfs로 물 영역을 구한다.
2. 각 영역별 인덱스를 한 개씩 저장한다.
2. union find로 매번 두 개의 L이 같은 그룹일 때까지 얼음을 녹인다.
2-2. bfs 탐색
2-3. x를 만나면 더이상 큐에 넣지 않고 해당 좌표를 방문처리 후 continue

두 번째 시도
1. bfs로 물 영역을 구한다.
2. x에 도착하면 x 좌표를 벡터에 따로 보관
3. union find로 매번 두 개의 L이 같은 그룹일 때까지 얼음을 녹인다.
3-1. 현재 좌표를 녹이고 인접한 곳에 X 탐색 후 존재하면 벡터에 추가한다.
*/

#pragma warning(disable:4996)
#include <stdio.h>
#include <vector>
using namespace std;
constexpr int N = 1500;
constexpr int M = 1500;
struct Node{
    int x, y;
}que[N * M];

struct Temp{
    int a, b, c;
    Temp(int x, int y, int z) : a{ x }, b{ y }, c{ z } {}
    Temp() {}
};
vector<Temp> arr;
char matrix[1500][1501];
int n, m, sx, sy, ex, ey, num, p[N * M / 2 + 1];
int visit[1500][1500], front, rear, dire[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
int find(int node) { return node == p[node] ? node : (p[node] = find(p[node])); }
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx < fy)
        p[fy] = fx;
    else if (fx > fy)
        p[fx] = fy;
}
void bfs(int x, int y)
{
    front = rear = -1;
    que[++rear] = { x, y };
    visit[x][y] = ++num;
    while (front != rear)
    {
        Node tmp = que[++front];
        for (int(&i)[2] : dire)
        {
            int tx = tmp.x + i[0], ty = tmp.y + i[1];
            if (!(0 <= tx && tx < n && 0 <= ty && ty < m)) continue;
            if(visit[tx][ty]) continue;
            visit[tx][ty] = num;
            if (matrix[tx][ty] == 'X')
                arr.emplace_back(tx, ty, num);
            else
                que[++rear] = { tx, ty };
        }
    }
}
void melt()
{
    vector<Temp> tmp = {};
    for (auto& [a, b, c] : arr)
    {
        matrix[a][b] = '.';
        if (visit[a][b] && visit[a][b] != c)
            Union(visit[a][b], c);
        else
            visit[a][b] = c;

        for (int(&i)[2] : dire)
        {
            int tx = a + i[0], ty = b + i[1];
            if (!(0 <= tx && tx < n && 0 <= ty && ty < m)) continue;
            if (matrix[tx][ty] != 'X' && visit[tx][ty] != c)
            {
                Union(visit[tx][ty], c);
                continue;
            }
            if (matrix[tx][ty] == 'X' && !visit[tx][ty])
            {
                visit[tx][ty] = c;
                tmp.emplace_back(tx, ty, c);
            }
        }
    }
    arr = tmp;
}
void init()
{
    scanf("%d%d", &n, &m);
    sx = -1;
    for (int i = 0; i < n; i++)
    {
        scanf("%s", matrix[i]);
        for (int j = 0; matrix[i][j]; j++)
        {
            if (matrix[i][j] == 'L')
            {
                matrix[i][j] = '.';
                if (sx < 0)
                {
                    sx = i;
                    sy = j;
                }
                else
                {
                    ex = i;
                    ey = j;
                }
            }
        }
    }
}
void solution()
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (matrix[i][j] != 'X' && !visit[i][j])
                bfs(i, j);
    for (int i = 0; i <= num; i++) p[i] = i;

    /*printf("\n");*/
    int ans = 0;
    while (find(visit[sx][sy]) != find(visit[ex][ey]))
    {
        melt();
        ans++;
        /*for (int i = 0; i < n; i++)
            printf("%s\n", matrix[i]);
        printf("\n");*/

    }
    printf("%d", ans);
    /*printf("\n");
    for (int i = 0; i <= num; i++)
        printf("%d ", p[i]);*/
}
int main()
{
    init();
    solution();
    
    return 0;
}