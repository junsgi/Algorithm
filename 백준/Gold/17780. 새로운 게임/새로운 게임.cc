#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
struct Node
{
	int num, dire, x, y;
	Node(int a, int b, int c, int d) : num(a), dire(b), x(c), y(d) {}
};
int n, k, map[12][12], d[4][2] = { {0, 1}, {0, -1}, {-1, 0}, {1, 0} };
vector<Node> horse[10];
int inRange(int x, int y) { return 0 <= x && x < n && 0 <= y && y < n; }
void stack(Node& node, int tx, int ty)
{
	for (auto& [_, __, a, b] : horse[node.num])
		a = tx, b = ty;
	auto [num, dire, x, y] = node;

	for (int i = 0; i < k; ++i)
	{
		if (i == num) continue;
		if (!horse[i].empty() && horse[i][0].x == x && horse[i][0].y == y)
		{
			for (auto [a, b, c, d] : horse[num])
				horse[i].emplace_back(a, b, c, d);
			horse[num].clear();
			break;
		}
	}
}
void move_(Node& node, int depth)
{
	auto [num, dire, x, y] = node;
	int tx = x + d[dire][0], ty = y + d[dire][1];
	if (!inRange(tx, ty) || map[tx][ty] == 2) // 파랑
	{
		if (depth) return;
		node.dire ^= 1;
		move_(node, 1);
	}
	else if (!map[tx][ty]) // 흰색
		stack(node, tx, ty);
	else // 빨강
	{
		for (int i = 0; i < horse[num].size() >> 1; ++i)
		{
			Node tmp = horse[num][i];
			horse[num][i] = horse[num][horse[num].size() - i - 1];
			horse[num][horse[num].size() - i - 1] = tmp;
		}
		if (horse[num][0].num != num)
			for (Node tmp : horse[num]) horse[horse[num][0].num].push_back(tmp);
		Node& tmp = horse[horse[num][0].num][0];
		if (horse[num][0].num != num)
			horse[num].clear();
		stack(tmp, tx, ty);
	}
	
}
void test()
{
	n = 3; k = 4;
	map[0][0] = 1; map[0][2] = 2;
	horse[0].emplace_back(0, 0, 0, 1);
	horse[0].emplace_back(1, 0, 0, 1);
	horse[0].emplace_back(2, 0, 0, 1);
	horse[3].emplace_back(3, 2, 0, 0);
}
int main()
{
	
	cin.tie(nullptr); cout.tie(nullptr);
	ios_base::sync_with_stdio(false);
	cin >> n >> k;
	for (int i = 0; i < n * n; ++i) cin >> map[i / n][i % n];
	for (int i = 0; i < k; ++i)
	{
		int a, b, c;
		cin >> a >> b >> c; --a; --b; --c;
		horse[i].emplace_back(i, c, a, b);
	}
	//test();
	for(int cnt = 1 ; cnt <= 1000; ++cnt)
	{
		for (int i = 0; i < k; ++i)
		{
			if (horse[i].empty()) continue;
			move_(horse[i][0], 0);
			for (int i = 0; i < k; ++i)
			{
				if (horse[i].size() >= 4)
				{
					cout << cnt;
					return 0;
				}
			}
		}
		
	}
	cout << -1;
	return 0;
}
/*
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
1 2 1
3 3 2
1 2 2
2 4 1
*/