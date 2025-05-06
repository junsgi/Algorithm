#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
struct Node
{
	int x, y, node;
	Node(int a, int b, int c) : x(a), y(b), node(c) {};
};
int cmp(const Node& x, const Node& y) { return x.x < y.x || (x.x == y.x && x.y > y.y); }
int n, m, MAX, ans[500000];
vector<Node> arr;
int main()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		if (a <= b)
		{
			arr.emplace_back(a, b, i);
			arr.emplace_back(a + n, b + n, i);
		}
		else
			arr.emplace_back(a, b + n, i);
	}
	sort(arr.begin(), arr.end(), cmp);
	for (int i = 0; i < arr.size(); i++)
	{
		if (arr[i].y <= MAX) ans[arr[i].node] = 1; // y는 내림차순, 최댓값보다 작거나 같다면 해당 노선은 포함시킴
		else MAX = arr[i].y;
	}
	for (int i = 0; i < m; i++)
		if (!ans[i]) printf("%d ", i + 1);
	return 0;
}