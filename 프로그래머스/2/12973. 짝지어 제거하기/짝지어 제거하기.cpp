#include <iostream>
#include<string>
using namespace std;

int solution(string s)
{
    int answer = 0;
    char stk[1000000] = {0, };
    int idx = -1;
    for(int i = 0 ; i < s.length() ; i++)
    {
        if (idx == -1 || s[i] != stk[idx])
            stk[++idx] = s[i];
        else
        {
            idx--;
        }
    }
    return idx == -1;
}