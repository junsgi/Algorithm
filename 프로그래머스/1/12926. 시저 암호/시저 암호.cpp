#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for(char& i : s)
    {
        if ('a' <= i)
            answer += ((i - 'a' + n) % 26 + 'a');
        else if ('A' <= i)
            answer += ((i - 'A' + n) % 26 + 'A');
        else
            answer += i;
    }
    return answer;
}