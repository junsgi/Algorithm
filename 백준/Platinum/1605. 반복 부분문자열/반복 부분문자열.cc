#include<stdio.h>
#include<vector>
#define MAX(x, y)((x) > (y)?(x):(y))
#define M 100003
using namespace std;
int n;
char* input;
vector<int> HASH[M];
int compare(int x, int y, int len)
{
    for (int i = 0; i < len; i++)
    {
        if (input[x + i] != input[y + i])
            return 0;
    }
    return 1;
}
// 롤링 해시 알고리즘
/*
* 문자열 abcd, 윈도우 크기 3, k = prime ^ (윈도우 크기 - 1)
* 각 문자열마다 소수를 누적곱하여 아래와 같이 해시 키를 만든다.
* H("abc") -> ("a" x prime ^ 2) + ("b" x prime ^ 1) + ("c" x prime ^ 0)
* 
* 가장 왼쪽에 있는 문자를 빼주어야 하므로 미리 만들어놓은 k를 이용하여 빼준다.
* 소수를 계속 곱해주는 이유는 왼쪽 문자가 빠진 후 key가 현재 ("b" x prime ^ 1) + ("c" x prime ^ 0) 상태이기 때문에
* 소수를 한 번 더 곱해주어 ("b" x prime ^ 2) + ("c" x prime ^ 1) 상태로 만든다.
* 그리고 문자를 더함
* H("bcd") -> (H("abc") - ("a" * k)) x prime + "d"
*/
int chk(int mid)
{
    for (int i = 0; i < M; i++)
        HASH[i].clear();
    int key = 0, p = 53, k = 1;
    for (int i = 0; i < n; i++)
    {
        if (i + 1 < mid) k = (k * p) % M;
        if (i + 1 > mid)
        {
            key = (key - ((input[i - mid] - 96) * k)) % M;
            key = (key + M) % M;
        }
        key = key * p;
        key = (key + (input[i] - 96)) % M;
        if (i + 1 >= mid)
        {
            for (int j = 0; j < HASH[key].size(); j++)
            {
                if (compare(i - mid + 1, HASH[key][j], mid))
                    return 1;
            }
            HASH[key].push_back(i - mid + 1);
        }
    }
    return 0;
}
int main()
{
    int answer = 0;
    scanf("%d", &n);
    input = new char[n + 1];
    scanf("%s", input);
    int left = 0, right = n;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (chk(mid))
        {
            left = mid + 1;
            answer = MAX(answer, mid);
        }
        else
            right = mid - 1;
    }
    printf("%d", answer);
    delete[] input;
    return 0;
}