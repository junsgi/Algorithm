#include<iostream>
#include<string>
#include<vector>
#define fastio cin.tie(nullptr);cout.tie(nullptr);ios_base::sync_with_stdio(false);
using namespace std;
int n, dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
char map[6][6];
vector<pair<int, int>> teacher;
string check()
{
	for (auto& [x, y] : teacher)
	{
		for (int(&d)[2] : dire)
		{
			int tx = x + d[0], ty = y + d[1];
			while (0 <= tx && tx < n && 0 <= ty && ty < n)
			{
				if (map[tx][ty] == 'S') return "NO";
				if (map[tx][ty] == 'O') break;
				tx += d[0]; ty += d[1];
			}
		}
	}
	return "YES";
}
string p(int idx, int cnt)
{
	if (idx == n * n) return "NO";
	if (cnt == 3)
		return check();
	string res = "NO";
	int x = idx / n, y = idx % n;
	if (map[x][y] != 'X')
		res = p(idx + 1, cnt);
	else
	{
		map[x][y] = 'O';
		res = p(idx + 1, cnt + 1);
		if (res == "YES") return res;
		map[x][y] = 'X';
		res = p(idx + 1, cnt);
	}
	return res;
}
int main()
{
	fastio;
	cin >> n;
	for (int i = 0; i < n * n; ++i)
	{
		cin >> map[i / n][i % n];
		if (map[i / n][i % n] == 'T')
			teacher.emplace_back(i / n, i % n);
	}
	cout << p(0, 0);
	return 0;
}