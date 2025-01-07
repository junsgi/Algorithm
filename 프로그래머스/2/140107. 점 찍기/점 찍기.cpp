#include <string>
#include <vector>
typedef long long ll;
using namespace std;

ll solution(int k, int d) {
    ll x = 0;
    ll y = d / (ll)k * (ll)k;
    ll answer = 0;
    while (x <= d && y >= 0)
    {
        if (x * x + y * y > (ll)d * (ll)d)
            y -= k;
        else
        {
            answer += y / (ll)k + 1L;
            x += k;
        }
    }
    return answer;
}