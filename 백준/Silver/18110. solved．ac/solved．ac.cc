#pragma warning(disable:4996)
#include<stdio.h>
#include<cmath>
using namespace std;
int n, arr[300'000], temp[300'000], cut;
double s;
void sort(int left, int right, int mid)
{
    int l = left, r = mid + 1;
    int idx = 0;
    while (l <= mid && r <= right)
    {
        if (arr[l] < arr[r])
            temp[idx] = arr[l++];
        else
            temp[idx] = arr[r++];
        idx++;
    }
    while (l <= mid) temp[idx++] = arr[l++];
    while (r <= right) temp[idx++] = arr[r++];
    for (int i = 0; i < idx; i++)
        arr[left + i] = temp[i];
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
    cut = (int)round(n * 0.15);
    if (n == 0)
    {
        printf("0");
        return 0;
    }
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    merge(0, n - 1);
    for (int i = cut; i < n - cut; i++)
        s += arr[i];
    int idx = n - cut * 2;
    printf("%d", (int)round(s / idx));
    return 0;
}
