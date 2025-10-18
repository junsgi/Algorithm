#include<iostream>
#include<algorithm>
using namespace std;
int n, m, _rank[1001], score[1001][3];
int equals(int a, int b)
{
	return score[a][0] == score[b][0] && score[a][1] == score[b][1] && score[a][2] == score[b][2];
}
int cmp(int a, int b)
{
	return score[a][0] > score[b][0] ||
		score[a][0] == score[b][0] && score[a][1] > score[b][1] ||
		score[a][0] == score[b][0] && score[a][1] == score[b][1] && score[a][2] > score[b][2];
}
int main() 
{
	cin >> n >> m;
	for(int _ = 0 ; _ < n; ++_)
	{
		int a;
		cin >> a;
		_rank[a] = 1;
		cin >> score[a][0] >> score[a][1] >> score[a][2];
	}
	for (int i = 1; i <= n; ++i)
	{
		for (int j = 1; j <= n; ++j)
		{
			if (i == j) continue;
			if (!equals(i, j) && cmp(i, j))
				++_rank[j];
		}
	}
	cout << _rank[m];
}