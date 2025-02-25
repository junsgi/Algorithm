#include <string>
#include <vector>
#include <iostream>
using namespace std;
void step1(string& id);
void step2(string& id);
void step3(string& id);
void step4(string& id);
void step5(string& id);
void step6(string& id);
void step7(string& id);
string solution(string new_id) {
    step1(new_id);
    step2(new_id);
    step3(new_id);
    step4(new_id);
    step5(new_id);
    step6(new_id);
    step7(new_id);
    cout << new_id << '\n';
    return new_id;
}

void step1(string& id)
{
    for(int i = 0 ; i < id.length(); i++)
        if ('A' <= id[i] && id[i] <= 'Z')
            id[i] = id[i] + 32;
}
void step2(string& id)
{
    string result = "";
    for(int i = 0 ; i < id.length(); i++)
    {
        if ('a' <= id[i] && id[i] <= 'z' ||
           '0' <= id[i] && id[i] <= '9' ||
           id[i] == '-' ||
           id[i] == '_' ||
           id[i] == '.')
            result += id[i];
    }
    id = result;
}
void step3(string& id)
{
    int cnt = 0;
    string result = "";
    for(auto& i : id)
    {
        if (i == '.')
            cnt++;
        else
        {
            if (cnt)
                result += '.';
            result += i;
            cnt = 0;
        }
    }
    if (cnt) result += '.';
    id = result;
}
void step4(string& id)
{
    string result = "";
    for(int i = 0 ; i < id.length(); i++)
    {
        if ((i == 0 || i == id.length() - 1) && id[i] == '.') continue;
        result += id[i];
    }
    id = result;
}
void step5(string& id)
{
    if(id.length() == 0)
        id += 'a';
}
void step6(string& id)
{
    string result = "";
    for(int i = 0 ; i < (15 < id.length() ? 15 : id.length()); i++)
        result += id[i];
    step4(result);
    id = result;
}
void step7(string& id)
{
    while (id.length() < 3)
        id += id[id.length() - 1];
}
