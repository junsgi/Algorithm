#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    string answer = "";
    for (auto s : myString)
    {
        if (s == 65 || s == 97)
            answer += "A";
        else if ('A' <= s && s <= 'Z' || 'a' <= s && s <= 'Z')
            answer += s <= 'Z' ? s + 32 : s;
        else
            answer += s;
    }
    return answer;
}