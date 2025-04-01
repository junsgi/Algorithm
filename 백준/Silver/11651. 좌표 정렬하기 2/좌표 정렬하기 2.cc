#include<stdio.h>
int n, x[100'000], y[100'000], tx[100'000], ty[100'000];
void sort(int left, int right, int mid)
{
    int l = left, r = mid + 1;
    int idx = 0;
    while (l <= mid && r <= right)
    {
        if (y[l] < y[r] || y[l] == y[r] && x[l] < x[r])
        {
            tx[idx] = x[l];
            ty[idx] = y[l];
            l++;
        }
        else
        {
            tx[idx] = x[r];
            ty[idx] = y[r];
            r++;
        }
        idx++;
    }
    while (l <= mid)
    {
        tx[idx] = x[l];
        ty[idx++] = y[l++];
    }
    while (r <= right)
    {
        tx[idx] = x[r];
        ty[idx++] = y[r++];
    }
    for (int i = 0; i < idx; i++)
    {
        x[left + i] = tx[i];
        y[left + i] = ty[i];
    }
}
void merge(int left, int right)
{
    if (left >= right) return;
    int mid = (left + right) / 2;
    merge(left, mid);
    merge(mid + 1, right);
    sort(left, right, mid);
}
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d%d", &x[i], &y[i]);
    merge(0, n - 1);
    for (int i = 0; i < n; i++)
        printf("%d %d\n", x[i], y[i]);
    return 0;
}
