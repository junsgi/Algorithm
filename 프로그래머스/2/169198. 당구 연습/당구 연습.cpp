#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int pow(int a) {return a * a;}
vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;
    int tx = 0, ty = 0;
    int bx = 0, by = 0;
    for(int i = 0 ; i < balls.size() ; i++)
    {
        int ans = 0x7fffffff;
        bx = balls[i][0]; by = balls[i][1];
        if (startY == by)
        {
            ans = min(ans, pow(startX - bx) + pow(n * 2 - startY - by));
            ans = min(ans, pow(startX - bx) + pow(-startY - by));
            if (startX < bx)
                ans = min(ans, pow(-startX - bx));
            else
                ans = min(ans, pow(m * 2 - startX - bx));
        }
        else if (startX == bx)
        {
            ans = min(ans, pow(-startX - bx) + pow(startY - by));
            ans = min(ans, pow(m * 2 - startX - bx) + pow(startY - by));
            if (startY < by)
                ans = min(ans, pow(-startY - by));
            else
                ans = min(ans, pow(n * 2 - startY - by));
        }
        else
        {
            ans = min(ans, pow(startX - bx) + pow(n * 2 - startY - by));
            ans = min(ans, pow(startX - bx) + pow(-startY - by));
            ans = min(ans, pow(-startX - bx) + pow(startY - by));
            ans = min(ans, pow(m * 2 - startX - bx) + pow(startY - by));
        }
        answer.push_back(ans);
    }
    return answer;
}