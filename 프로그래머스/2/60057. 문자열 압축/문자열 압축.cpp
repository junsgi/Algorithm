#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(string s) {
    int answer = s.length();
    for(int i = 1; i < s.length() ; i++)
    {
        int start = 0;
        string standard = s.substr(start, i);
        string result = "";
        string temp = "";
        start = i;
        int cnt = 1;
        
        while (start < s.length())
        {
            temp = s.substr(start, i);
            if (!standard.compare(temp))
                cnt++;
            else
            {
                if (cnt == 1) result += standard;
                else result += to_string(cnt) + standard;
                standard = temp;
                cnt = 1;
            }
            start += i;
        }
        if (cnt == 1) result += temp;
        else result += to_string(cnt) + temp;
        answer = min(answer, (int)result.length());
    }
    return answer;
}