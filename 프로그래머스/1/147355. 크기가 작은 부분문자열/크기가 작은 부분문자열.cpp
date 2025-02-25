#include <string>
#include <vector>
using namespace std;
typedef unsigned long long ull;
ull g(int idx, int len, string& t)
{
    ull result = 0;
    for(int i = idx; i < idx + len ; i++)
        result = result * 10 + (ull)(t[i] - '0');
    return result;
}
int solution(string t, string p) {
    int answer = 0;
    int len = p.length();
    ull P = g(0, len, p);
    ull T = 0;
    for(int i = 0 ; i <= t.length() - len; i++)
    {
        ull tmp = g(i, len, t);
        if (tmp <= P)answer++;
    }
    return answer;
}