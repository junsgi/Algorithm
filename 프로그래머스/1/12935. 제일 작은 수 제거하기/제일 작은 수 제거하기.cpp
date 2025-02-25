#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    if (arr.size() == 1) return {-1};
    vector<int> answer;
    int MIN = 0x7fffffff;
    for(int& i:arr)
        MIN = MIN > i ? i : MIN;
    for(int& i:arr)
        if (i != MIN) answer.push_back(i);
    return answer;
}