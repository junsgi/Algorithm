// 음수 간선이 존재하므로 벨만 포드 알고리즘을 사용하여 최단거리와 사이클 판단
#pragma warning(disable:4996)
#include<iostream>
#include<vector>
#include<algorithm>
#define M 987543210
using namespace std;
typedef pair<int, int> pii;
struct Node
{
    int x, y, z;
    Node(int a, int b, int c) : x(a), y(b), z(c) {}
};
int w, h, g, matrix[30][30], ck[900], dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int cost[900];
vector<Node> arr;
int getNode(int x, int y) { return x * w + y; }
void make_arr()
{
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (i == h - 1 && j == w - 1) break;
            int node = getNode(i, j);
            // 묘비거나 귀신 구멍이라면 continue, 묘비 = -1, 구멍 = 1
            if (ck[node] != 0) continue;
            for (const int* k : dire)
            {
                int tx = i + (*k), ty = j + *(k + 1);
                if (!(0 <= tx && tx < h && 0 <= ty && ty < w)) continue;
                int tnode = getNode(tx, ty);
                if (ck[tnode] < 0) continue; // 묘비면 continue
                arr.emplace_back(node, tnode, 1);
            }
        }
    }
}
void init()
{
    fill(&matrix[0][0], &matrix[0][0] + w * h, 0);
    fill(cost, cost + w * h, M);
    fill(ck, ck + w * h, 0);
    arr.clear();
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    while (1)
    {
        cin >> w >> h;
        if (w + h == 0) break;

        // init
        init();

        cin >> g;
        for (int i = 0; i < g; i++)
        {
            int a, b;
            cin >> a >> b;
            ck[getNode(b, a)] = -1;
        }

        cin >> g;
        for (int i = 0; i < g; i++)
        {
            int a, b, c, d, e;
            cin >> a >> b >> c >> d >> e;
            arr.emplace_back(getNode(b, a), getNode(d, c), e);
            ck[getNode(b, a)] = 1;
        }

        make_arr();

        // bellman ford Algorithm
        cost[0] = 0;
        int hit = 0;
        for (int i = 0; i <= w * h; i++)
        {
            hit = 0;
            for (const struct Node& ref : arr)
            {
                if (cost[ref.x] == M) continue;
                if (cost[ref.x] + ref.z < cost[ref.y])
                {
                    hit = 1;
                    cost[ref.y] = cost[ref.x] + ref.z;
                }
            }
        }
        if (hit == 1)
            cout << "Never\n";
        else if (cost[getNode(h - 1, w - 1)] == M)
            cout << "Impossible\n";
        else
            cout << cost[getNode(h - 1, w - 1)] << '\n';
    }

    return 0;
}