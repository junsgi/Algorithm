#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
int n, arr[1001], ans;
priority_queue<pair<int, int>, vector<pair<int, int>>> heap;
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        heap.push({ b, a });
    }
    while (!heap.empty())
    {
        pair<int, int> element = heap.top(); heap.pop();
        for (int i = element.second; i >= 1; i--)
        {
            if (arr[i] == 0)
            {
                arr[i] = 1;
                ans += element.first;
                break;
            }
        }
    }
    printf("%d", ans);
    return 0;
}
