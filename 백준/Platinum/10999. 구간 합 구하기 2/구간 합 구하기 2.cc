/*
느리게 갱신되는 세그먼트 트리

원소의 개수(N)는 최대 100만 개, 수정 질의 수(M)는 최대 10'000
최악의 경우 시간 복잡도는 약 O(10'000 * 1'000'000 * 2)

아이디어는 다음과 같다.
수정은 첫 번째부터 100만 번째까지 수정하지만 쿼리의 구간은 짧다면 **필요한 구간에만 값을 갱신해 주는 것이다**.

수정과 쿼리는 재귀로 구현하였고, 탐색 중 두 자식의 합이 부모의 값과 다르다면 값을 갱신하고
원하는 구간에 도착하면 리턴한다.
*/
#include <iostream>
using namespace std;
using ll = long long;
int a, b, c, x;
ll n, m, k, seg[1 << 21], tmp, d;
ll update(int left, int right, int idx, int st, int ed, ll value)
{
    if (ed < left || right < st) return seg[idx];

    // 느린 갱신
    int child = idx << 1;
    if (child < (x << 1) && seg[idx] != seg[child] + seg[child | 1])
    {
        tmp = (seg[idx] - (seg[child] + seg[child | 1])) >> 1;
        seg[child] += tmp; seg[child | 1] += tmp;
    }
    if (st <= left && right <= ed) // 원하는 구간이면 리턴
        return seg[idx] += value * (right - left + 1);
    
    int mid = left + right >> 1;
    return seg[idx] = update(left, mid, idx << 1, st, ed, value) + update(mid + 1, right, idx << 1 | 1, st, ed, value);
}
void insert(int idx, ll value)
{
    --idx |= x;
    seg[idx] = value;
    while (idx >>= 1)
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1];
}
ll query(int left, int right, int idx, int st, int ed)
{
    if (ed < left || right < st) return 0;

    // 느린 갱신
    int child = idx << 1;
    if (child < (x << 1) && seg[idx] != seg[child] + seg[child | 1])
    {
        tmp = (seg[idx] - (seg[child] + seg[child | 1])) >> 1;
        seg[child] += tmp; seg[child | 1] += tmp;
    }
    if (st <= left && right <= ed) return seg[idx]; // 원하는 구간이면 리턴
    
    int mid = left + right >> 1;
    return query(left, mid, idx << 1, st, ed) + query(mid + 1, right, idx << 1 | 1, st, ed);
} 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n >> m >> k;
    for (x = 1; x < n; x <<= 1);
    for (int i = 1 ; i <= n ; i++)
    {
        cin >> tmp;
        insert(i, tmp);
    }
    for (int _ = 0; _ < m + k; _++)
    {
        cin >> a >> b >> c;
        if (a & 1)
        {
            cin >> d;
            update(1, x, 1, b, c, d);
        }
        else
            cout << query(1, x, 1, b, c) << '\n';
    }
    return 0;
}