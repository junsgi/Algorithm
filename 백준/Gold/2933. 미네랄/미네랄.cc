#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using pii = pair<int, int>;
int r, c, n, t, front, rear, cnt, visit[100][100], dire[4][2] = { {1, 0}, {0, -1}, {0, 1}, { -1, 0 } };
pii que[100 * 100];
string matrix[100];
vector<pii> bfs(int x, int y) 
{
    vector<pii> boundary = {};
    front = rear = -1;
    que[++rear] = { x, y };
    visit[x][y] = ++cnt;
    matrix[x][y] = '.';
    while (front != rear)
    {
        auto& [a, b] = que[++front];
        int hit = 0;
        for (int(&i)[2] : dire)
        {
            int tx = a + i[0], ty = b + i[1];
            if (!(0 <= tx && tx < r && 0 <= ty && ty < c)) continue;
            if (matrix[tx][ty] == '.' && visit[tx][ty] != cnt) { hit = 1; continue; }
            if (visit[tx][ty] == cnt) continue;
            matrix[tx][ty] = '.';
            visit[tx][ty] = cnt;
            que[++rear] = { tx, ty };
        }
        if (hit)
            boundary.emplace_back(a, b);
    }
    
    return boundary;
}

void down(vector<pii> arr)
{
    int x = 0, hit = 0;
    while (!hit)
    {
        x++;
        for (int i = 0; !hit && i < arr.size(); i++)
        {
            if (arr[i].first + x >= r || matrix[arr[i].first + x][arr[i].second] == 'x')
                hit = 1;
        }
    }
    x--;
    for (int i = 0; i <= front; i++)
        matrix[que[i].first + x][que[i].second] = 'x';
}
void pro(int x, int y)
{
    matrix[x][y] = '.';
    for (int(&i)[2] : dire)
    {
        int tx = x + i[0], ty = y + i[1];
        if (!(0 <= tx && tx < r && 0 <= ty && ty < c)) continue;
        if (matrix[tx][ty] == '.') continue;
        down(bfs(tx, ty));
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> r >> c;
    for (int i = 0; i < r; i++)
        cin >> matrix[i];
    
    cin >> n;
    for(int i = 0 ; i < n ; i++)
    {
        cin >> t;
        
        for (int j = 0; ~i & 1 && j < c; j++)
        {
            if (matrix[r - t][j] == '.') continue;
            pro(r - t, j);
            break;
        }
        for (int j = c - 1; i & 1 && j >= 0; j--)
        {
            if (matrix[r - t][j] == '.') continue;
            pro(r - t, j);
            break;
        }
    }
    for (int i = 0; i < r; i++)
        cout << matrix[i] << '\n';
    return 0;
}
