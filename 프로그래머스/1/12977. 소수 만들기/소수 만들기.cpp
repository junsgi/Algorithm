#include <vector>
using namespace std;
int isPrime(int n);
int sqrt(int n);
int solution(vector<int> nums) {
    int answer = 0;
    for(int i = 0 ; i < nums.size() ; i++)
        for(int j = i + 1; j < nums.size() ; j++)
            for(int k = j + 1; k < nums.size() ; k++)
                if (isPrime(nums[i] + nums[j] + nums[k]))
                    answer++;
    return answer;
}

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

int isPrime(int n)
{
    for(int i = 2 ; i <= sqrt(n) ; i++)
        if (n % i == 0) return 0;
    return 1;
}