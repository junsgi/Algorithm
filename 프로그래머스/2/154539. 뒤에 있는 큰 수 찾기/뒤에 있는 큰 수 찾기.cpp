#include <string>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int, int> pii;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    for(int i = 0 ; i < numbers.size() ; i++) answer.push_back(-1);
    pii stk[1'000'000] = {{}, };
    int idx = -1;
    for(int i = 0 ; i < numbers.size() ; i++)
    {
        if (idx == -1 || stk[idx].first >= numbers[i])
            stk[++idx] = {numbers[i], i};
        else
        {
            while (1)
            {
                if (idx == -1 || stk[idx].first >= numbers[i])
                    break;
                answer[stk[idx--].second] = numbers[i];
            }
            stk[++idx] = {numbers[i], i};
        }
    }
    return answer;
}