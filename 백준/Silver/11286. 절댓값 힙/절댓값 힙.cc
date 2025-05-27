#pragma warning(disable:4996)
#include<stdio.h>
int abs(int a) { return a < 0 ? -a : a; }
struct Node
{
    int n, origin;
    bool operator<(const Node& x) const {
        return (n < x.n) || (n == x.n && origin < x.origin);
    }
}heap[100001];
int n, len;
void up(int idx)
{
    if (idx / 2 <= 0) return;
    if (heap[idx] < heap[idx / 2])
    {
        Node tmp = heap[idx]; heap[idx] = heap[idx / 2]; heap[idx / 2] = tmp;
        up(idx / 2);
    }
}
void down(int idx)
{
    int child = idx * 2;
    if (child > len) return;
    if (child + 1 <= len && heap[child + 1] < heap[child]) child++;
    if (heap[child] < heap[idx])
    {
        Node tmp = heap[idx]; heap[idx] = heap[child]; heap[child] = tmp;
        down(child);
    }
}
int main()
{
    scanf("%d", &n);
    while (n--)
    {
        int a;
        scanf("%d", &a);
        if (!a)
        {
            if (len)
            {
                printf("%d\n", heap[1].origin);
                heap[1] = heap[len--];
                down(1);
            }
            else
                printf("0\n");
        }
        else
        {
            heap[++len] = {abs(a), a};
            up(len);
        }
    }
    return 0;
}