// 고도를 정렬 후 최소 최댓값을 정한다.
// 탐색 경로의 고도가 최소 최댓값 사이를 유지하면서 모든 마을에 도착했다면 성공
// 성공했다면 돌아오는길은 갔던 길로 돌아오면 되므로 구현x
#include<iostream>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
struct Node {
	int x, y;
	Node(int tx, int ty) : x(tx), y(ty) {}
};
int n, cost[50][50], sx, sy, cnt, ans, visit[50][50], dire[8][2] = { {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1} };
string graph[50];
queue<Node> que;
vector<int> arr;
void init()
{
	ans = 0x7fffffff;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> graph[i];
		for (int j = 0; j < n; j++)
		{
			if (graph[i][j] == 'P')
			{
				sx = i;
				sy = j;
				graph[i][j] = '.';
			}
			if (graph[i][j] == 'K')
				cnt++;
		}
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			cin >> cost[i][j];
			arr.emplace_back(cost[i][j]);
		}
}

int bfs(int a, int b)
{
	// 시작 위치가 범위에 들지 않으면 return
	if (!(a <= cost[sx][sy] && cost[sx][sy] <= b)) return 0;
	que = queue<Node>();
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			visit[i][j] = 0;
	int c = 0;
	int MIN = cost[sx][sy];
	int MAX = cost[sx][sy];
	que.emplace(sx, sy);
	visit[sx][sy] = 1;

	while (!que.empty())
	{
		Node t = que.front(); que.pop();
		MIN = min(MIN, cost[t.x][t.y]);
		MAX = max(MAX, cost[t.x][t.y]);

		for (const int(&i)[2] : dire)
		{
			int tx = t.x + i[0], ty = t.y + i[1];
			if (!(0 <= tx && tx < n && 0 <= ty && ty < n)) continue; // 범위
			if (visit[tx][ty]) continue; // 방문
			if (!(a <= cost[tx][ty] && cost[tx][ty] <= b)) continue; // 피로도
			if (graph[tx][ty] == 'K') c++; // 마을 방문 횟수
            MIN = min(MIN, cost[tx][ty]);
			MAX = max(MAX, cost[tx][ty]);
			if (c == cnt) // 모든 마을에 방문했다면 return 
			{
				ans = min(ans, MAX - MIN);
				return 1;
			}
			visit[tx][ty] = 1;
			que.emplace(tx, ty);

		}
	}
	return 0;
}

void solution()
{
	sort(arr.begin(), arr.end());
	int left = 0, right = 1;
	while (left <= right && right < arr.size())
	{
		if (bfs(arr[left], arr[right]))
			left++;
		else
			right++;
	}
	printf("%d", ans);
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	init();
	solution();
	return 0;
}