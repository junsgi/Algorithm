/*
보석은 무게를 기준으로 오름차순 정렬
가방도 오름차순 정렬

가방에 담을 수 있는 보석을 힙에 모두 삽입 (최대 힙)
가방보다 무게가 더 무겁다면 while문을 빠져나와 힙의 루트 값을 더한다.

이 과정을 k만큼 반복
*/
#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, k, bag[300000], len, heap[300001];
pair<int, int> jewel[300000];
long long ans;
int cmp(pair<int, int> x, pair<int, int> y)
{
	return x.first < y.first ;
}
void up(int idx)
{
	if (idx / 2 <= 0) return;
	if (heap[idx] < heap[idx / 2])
	{
		int tmp = heap[idx];
		heap[idx] = heap[idx / 2];
		heap[idx / 2] = tmp;
		up(idx / 2);
	}
}
void down(int idx)
{
	if (idx * 2 > len) return;

	int child = 0;
	if (heap[idx * 2] < heap[idx * 2 + 1])
		child = idx * 2;
	else
		child = idx * 2 + 1;

	if (heap[child] < heap[idx])
	{
		int tmp = heap[idx];
		heap[idx] = heap[child];
		heap[child] = tmp;
		down(child);
	}
}
int main()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		jewel[i] = {a, b};
	}
	for (int i = 0; i < k; i++)
		scanf("%d", &bag[i]);
	sort(jewel, jewel + n, cmp);
	sort(bag, bag + k);
	int idx = 0;
	for (int i = 0; i < k; i++)
	{
		while (idx < n && bag[i] >= jewel[idx].first)
		{
			heap[++len] = -jewel[idx++].second;
			up(len);
		}
		if (len) 
		{
			ans += -heap[1];
			heap[1] = heap[len--];
			down(1);
		}
	}
	printf("%lld", ans);
	return 0;
}
