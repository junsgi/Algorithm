#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    for(int i = 0 ; i < strArr.size() ; i++)
    {
        string temp = "";
        for(auto s : strArr[i])
        {
            if (i % 2 != 0)
                temp += s > 'Z'? s - 32 : s;
            else 
                temp += s <= 'Z'? s + 32 : s;
        }
        answer.push_back(temp);
        
    }
    return answer;
}