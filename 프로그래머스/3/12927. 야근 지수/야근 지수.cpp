#include <string>
#include <vector>
#include <iostream>
typedef long long ll;
using namespace std;

ll heap[20'200], len;
void ch(int x, int y)
{
    ll temp = heap[x];
    heap[x] = heap[y];
    heap[y] = temp;
}
void up(ll idx)
{
    if (idx / 2 <= 0) return;
    if (heap[idx] > heap[idx / 2])
    {
        ch(idx, idx / 2);
        up(idx / 2);
    }
}
void down(ll idx)
{
    ll child = idx * 2;
    if (child > len) return;
    if (child + 1 <= len and heap[child] < heap[child + 1]) child++;
    if (heap[idx] < heap[child])
    {
        ch(idx, child);
        down(child);
    }
}
ll solution(int n, vector<int> works) {
    ll answer = 0;
    for(int i = 0 ; i < (int)works.size(); i++)
    {
        heap[++len] = works[i];
        up(len);
    }
    while (n)
    {
        ll item = heap[1] - 1;
        n--;
        heap[1] = heap[len--];
        down(1);
        
        heap[++len] = item;
        up(len);
    }
    
    while (len)
    {
        if (heap[1] > 0)
            answer += heap[1] * heap[1];
        heap[1] = heap[len--];
        down(1);
    }
    return answer;
}