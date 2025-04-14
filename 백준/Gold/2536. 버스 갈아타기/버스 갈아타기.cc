#include<stdio.h>
#include<algorithm>
using namespace std;
typedef long long ll;
struct Loc {
	ll x1, y1, x2, y2, no;
}arr[5001];
ll n, m, k, sx, sy, ex, ey, que[5111];
int front, rear, visit[5001], path[5111];
int ccw(ll a, ll b, ll c, ll d, ll e, ll f)
{
	ll res = (a * d + c * f + e * b) - (c * b + e * d + a * f);
	if (res > 0) return 1;
	else if (res < 0) return -1;
	return 0;
}
void backtracking(int node)
{
	if (node == -1) return;
	backtracking(path[node]);
	printf("%lld ", arr[que[node]].no);
}
int main()
{	
	scanf("%lld%lld%lld", &m, &n, &k);
	for (int i = 0; i < k; i++)
	{
		ll a, b, c, d, e;
		scanf("%lld%lld%lld%lld%lld", &a, &b, &c, &d, &e); 
		a--; b--; c--; d--; e--;
		arr[a] = { b, c, d, e, a };
	}
	scanf("%lld%lld%lld%lld", &sx, &sy, &ex, &ey); sx--; sy--; ex--; ey--;

	arr[5000] = { sx, sy, sx, sy, 5000 };
	front = rear = -1;
	que[++rear] = 5000;
	visit[5000] = 1;
	path[0] = -1;
	while (front != rear)
	{
		Loc cur = arr[que[++front]];
		int depth = visit[cur.no];
		if (min(cur.x1, cur.x2) <= ex && ex <= max(cur.x1, cur.x2) && min(cur.y1, cur.y2) <= ey && ey <= max(cur.y1, cur.y2))
		{
			/*backtracking(front);*/
			printf("%d", depth - 1);
			return 0;
		}
		for (int i = 0; i < k; i++)
		{
			if (visit[arr[i].no]) continue;
			int c1 = ccw(cur.x1, cur.y1, cur.x2, cur.y2, arr[i].x1, arr[i].y1);
			int c2 = ccw(cur.x1, cur.y1, cur.x2, cur.y2, arr[i].x2, arr[i].y2);
			int c3 = ccw(arr[i].x1, arr[i].y1, arr[i].x2, arr[i].y2, cur.x1, cur.y1);
			int c4 = ccw(arr[i].x1, arr[i].y1, arr[i].x2, arr[i].y2, cur.x2, cur.y2);
			if (c1 * c2 == 0 && c3 * c4 == 0) // 일직선이면
			{
				// 겹치는지 확인
				int res = min(cur.x1, cur.x2) <= max(arr[i].x1, arr[i].x2) &&
					min(arr[i].x1, arr[i].x2) <= max(cur.x1, cur.x2) &&
					min(cur.y1, cur.y2) <= max(arr[i].y1, arr[i].y2) &&
					min(arr[i].y1, arr[i].y2) <= max(cur.y1, cur.y2);

				if (!res) continue;
				que[++rear] = arr[i].no;
				visit[arr[i].no] = depth + 1;
				path[rear] = front; // 역추적

			}
			else if (c1 * c2 <= 0 && c3 * c4 <= 0) // 교차 판정 
			{
				que[++rear] = arr[i].no;
				visit[arr[i].no] = depth + 1;
				path[rear] = front; // 역추적
			}
		}
	}
	return 0;
}
