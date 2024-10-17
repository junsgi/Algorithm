#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    string answer = "";
    for(auto i : myString) answer += i <= 'Z' ? i + 32 : i;
    return answer;
}