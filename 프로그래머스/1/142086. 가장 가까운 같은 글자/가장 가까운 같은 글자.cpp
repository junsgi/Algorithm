#include <string>
#include <vector>
using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int* ref = new int[26] {};
    for(int i = 0 ; i < 26 ; i++) ref[i] = -1;
    for(int i = 0 ; i < s.length() ; i++)
    {
        if (ref[s[i] - 'a'] == -1)
            answer.push_back(-1);
        else
            answer.push_back(i - ref[s[i] - 'a']);
        ref[s[i] - 'a'] = i;
    }
    delete[] ref;
    return answer;
}