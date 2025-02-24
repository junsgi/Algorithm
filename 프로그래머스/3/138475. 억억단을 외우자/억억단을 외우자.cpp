#include <vector>
#include <algorithm>
#include <iostream>
#define LEN 1<<24
using namespace std;
struct Temp
{
    int n, cnt;
};
int range;
Temp seg[LEN];
void init(int e);
Temp segInit(int left, int right, int idx);
Temp query(int left, int right, int idx, int start, int end);
vector<int> solution(int e, vector<int> starts) {
    vector<int> answer;
    init(e);
    for(auto& i : starts)
    {
        Temp result = query(1, range, 1, i, e);
        answer.push_back(result.n);
    }
    return answer;
}

void init(int e)
{
    int st = 1;
    for(; st <= e ; st *= 2);
    range = st;
    for(int i = 0; i < st * 2; i++)
    {
        seg[i].n = 9999999;
        seg[i].cnt = -9999999;
    }
    for(int i = 1; i <= e; i++)
        for(int j = i; j <= e; j += i)
        {
            if (seg[st + j - 1].cnt == -9999999)
                seg[st + j - 1].cnt = 0;
            seg[st + j - 1].n = j;
            seg[st + j - 1].cnt++;
        }
    segInit(1, st, 1);
    
    // for(int i = 1; i < st + e ; i++)
    //     cout << i << " " << seg[i].n << " " << seg[i].cnt << '\n';
}

Temp segInit(int left, int right, int idx)
{
    if (left == right) return seg[idx];
    int mid = (left + right) / 2;
    Temp l = segInit(left, mid, idx * 2);
    Temp r = segInit(mid + 1, right, idx * 2 + 1);
    if (l.cnt > r.cnt || l.cnt == r.cnt && l.n < r.n)
    {
        seg[idx].n = l.n;
        seg[idx].cnt = l.cnt;
        return l;
    }else
    {
        seg[idx].n = r.n;
        seg[idx].cnt = r.cnt;
        return r;
    }
}

Temp query(int left, int right, int idx, int start, int end)
{
    if (start <= left && right <= end) return seg[idx];
    if (end < left || right < start) return {9999999, -9999999};
    int mid = (left + right) / 2;
    Temp l = query(left, mid, idx * 2, start, end);
    Temp r = query(mid + 1, right, idx * 2 + 1, start, end);
    if (l.cnt > r.cnt || l.cnt == r.cnt && l.n < r.n)
        return l;
    else
        return r;
    
}
