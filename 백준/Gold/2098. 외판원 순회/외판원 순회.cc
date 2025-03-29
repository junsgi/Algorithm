/*
비트마스킹 활용
1 -> 2 -> 3 -> 4
DP[0b1111][4] = 39

1 -> 2 -> 4 -> 3
DP[0b1111][3] = 35
등 비트는 같아도 현재 위치에 따라서 값이 다양하게 나올 수 있음
*/
#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
#define M 100'000'000
using namespace std;
int n, DP[1 << 16][16], graph[16][16];
int min(int a, int b) { return a < b ? a : b; }
int memo(int node, int check)
{
	// 항상 순회할 수 있는 경우만 주어짐
	// 전부 방문했다면 현재 위치에서 원점으로 가는 값 리턴
	if (check == (1 << n) - 1) return graph[node][0];

	// 메모되어있으면 메모된 값 리턴
	if (DP[check][node] != 0) return DP[check][node];

	// DP 초기화
	DP[check][node] = M;
	for (int i = 0; i < n; i++)
	{
		// 방문했거나 길이 없다면 continue
		if (check & (1 << i) || graph[node][i] == M)continue;
		DP[check][node] = min(DP[check][node], memo(i, check | (1 << i)) + graph[node][i]);
	}
	return DP[check][node];
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &graph[i][j]);
			if (!graph[i][j])graph[i][j] = M;
		}
	}
	printf("%d", memo(0, 1));
	return 0;
}