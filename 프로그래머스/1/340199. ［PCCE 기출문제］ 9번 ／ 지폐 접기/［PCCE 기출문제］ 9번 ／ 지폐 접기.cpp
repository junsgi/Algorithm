#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int check(vector<int> &a, vector<int> &b)
{
    return min(a[0], a[1]) <= min(b[0], b[1]) && max(a[0], a[1]) <= max(b[0], b[1]);
}
int solution(vector<int> wallet, vector<int> bill) 
{
    int answer = 0;
    while (!check(bill, wallet))
    {
        if (bill[0] > bill[1])
            bill[0] /= 2;
        else
            bill[1] /= 2;
        answer++;
    }
    return answer;
}