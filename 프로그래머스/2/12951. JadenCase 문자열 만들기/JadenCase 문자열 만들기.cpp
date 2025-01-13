#include <string>
#include <vector>

using namespace std;
string solution(string s) {
    string answer = "";
    bool k = false;
    for(int i = 0 ; i < s.length() ; i++)
    {
        if (s[i] == ' ' || ('0' <= s[i] && s[i] <= '9'))
        {
            answer += s[i];
            if (s[i] == ' ')
                k = false;
            else
                k = true;
        }
        else if (!k)
        {
            answer += s[i] <= 'Z' ? s[i] : s[i] - 32;
            k = true;
        }else
            answer += s[i] <= 'Z' ? s[i] + 32 : s[i];
    }
    return answer;
}