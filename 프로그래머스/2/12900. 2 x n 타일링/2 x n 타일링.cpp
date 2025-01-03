#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int a = 0;
    int b = 1;
    int c = 1;
    for(int i = 1 ; i <= n ; i++)
    {
        c = a % 1'000'000'007 + b % 1'000'000'007;
        a = b % 1'000'000'007;
        b = c % 1'000'000'007;
    }
    return c % 1'000'000'007;
}