#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string myString) {
    string answer = "";
    for(auto i : myString) {
        if (i >= 'a') {
            i -= 32;
        }
        answer += i;
    }
    return answer;
}