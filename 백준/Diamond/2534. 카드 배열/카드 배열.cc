#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
#define M 1'000'000'007
using namespace std;
int n, k, p, c, heap[300'100], n1[300000], n2[300000], len;
long long po[300'000], MAX, MIN;
vector<int> g1[300'000], g2[300'000];
void up(int idx);
void down(int idx);
int main()
{
    scanf("%d%d%d", &n, &k, &p);
    po[0] = 1;
    for (int i = 1; i < k; i++)
        po[i] = po[i - 1] * n % M; 

    for (int i = 0; i < p; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        g1[b].emplace_back(a); n1[a]++;
        g2[a].emplace_back(b); n2[b]++;
    }
    
    c = n - k;
    for (int i = 0; i < k; i++)
    {
        if (!n1[i])
        {
            heap[++len] = i;
            up(len);
        }
    }
    while (len)
    {
        int node = heap[1];
        heap[1] = heap[len--]; down(1);
        MAX += (po[node] * (c++)) % M;
        MAX %= M;
        for (int& tnode : g1[node])
        {
            if (--n1[tnode] == 0)
            {
                heap[++len] = tnode;
                up(len);
            }
        }
    }

    len = 0;
    c = k;
    for (int i = 0; i < k; i++)
    {
        if (!n2[i])
        {
            heap[++len] = i;
            up(len);
        }
    }
    while (len)
    {
        int node = heap[1];
        heap[1] = heap[len--]; down(1);
        MIN += (po[node] * (--c)) % M;
        MIN %= M;

        for (int& tnode : g2[node])
        {
            if (--n2[tnode] == 0)
            {
                heap[++len] = tnode;
                up(len);
            }
        }
    }
    printf("%lld", ((MAX + M) - MIN) % M);
    return 0;
}

void up(int idx)
{
    if (idx / 2 <= 0) return;
    if (heap[idx] < heap[idx / 2])
    {
        int tmp = heap[idx]; heap[idx] = heap[idx / 2]; heap[idx / 2] = tmp;
        up(idx / 2);
    }
}
void down(int idx)
{
    int child = idx * 2;
    if (child > len) return;
    if (child + 1 <= len && heap[child] > heap[child + 1])child++;
    if (heap[idx] > heap[child])
    {
        int tmp = heap[idx]; heap[idx] = heap[child]; heap[child] = tmp;
        down(child);
    }
}
