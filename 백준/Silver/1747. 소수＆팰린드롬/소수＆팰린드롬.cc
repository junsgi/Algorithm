#include<stdio.h>
char temp[10];
int isPalindrome(long long n)
{
    int len = 0;
    while (n)
    {
        temp[len++] = n % 10 + '0';
        n /= 10;
    }
    for (int i = 0; i < len / 2; i++)
    {
        if (temp[i] != temp[len - i - 1])
            return 0;
    }
    return 1;
}
int root(long long n)
{
    long long left = 0, right = n - 1;
    while (left <= right)
    {
        long long mid = (left + right) / 2;
        if (mid * mid < n)
            left = mid + 1;
        else if (mid * mid > n)
            right = mid - 1;
        else
            return mid;
    }
    return right;
}
int isPrime(long long n)
{
    for (int i = 2; i <= root(n); i++)
        if (n % i == 0) return 0;
    return 1;
}
int main()
{
    long long n;
    scanf("%lld", &n);
    if (n == 1) n++;
    while (1)
    {
        if (isPrime(n) && isPalindrome(n))
        {
            printf("%lld", n);
            return 0;
        }
        n++;
    }
    return 0;
}