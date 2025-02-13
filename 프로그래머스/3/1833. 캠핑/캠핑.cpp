#include <vector>
#include <algorithm>
using namespace std;
int solution(int n, vector<vector<int>> data) {
    int answer = 0;
    sort(data.begin(), data.end());
    for(int i = 0 ; i < data.size() ; i++)
    {
        for(int j = i + 1 ; j < data.size(); j++)
        {
            if (abs(data[i][0] - data[j][0]) * abs(data[i][1] - data[j][1]) == 0) continue;
            bool hit = false;
            for(int k = i + 1 ; k < j; k++)
            {
                if (min(data[i][0], data[j][0]) < data[k][0] && data[k][0] < max(data[i][0], data[j][0]) &&
                   min(data[i][1], data[j][1]) < data[k][1] && data[k][1] < max(data[i][1], data[j][1]))
                    hit = true;
                if (hit) break;
            }
            if (!hit)answer++;
        }
    }
    return answer;
}