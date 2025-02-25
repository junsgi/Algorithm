#include <string>
#include <vector>
using namespace std;
int sqrt(int n)
{
    int left = 0;
    int right = n;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (mid * mid <= n)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return right;
}
int solution(int left, int right) {
    int answer = 0;
    for(;left <= right; left++)
    {
        int cnt = 0;
        for(int i = 1 ; i <= sqrt(left) ; i++)
        {
            if (i * i == left)
                cnt++;
            else if (left % i == 0)
                cnt += 2;
        }
        if (cnt&1)
            answer += -left;
        else
            answer += left;
    }
    return answer;
}