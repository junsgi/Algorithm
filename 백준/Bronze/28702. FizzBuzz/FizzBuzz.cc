#pragma warning(disable:4996)
#include<iostream>
#include<string>
#define MAX(x,y)((x)<(y)?(y):(x))
using namespace std;
int hit = -1;
string arr[3];
string print(int s)
{
    if (s % 3 == 0 && s % 5 == 0)
        return "FizzBuzz";
    else if (s % 3 == 0)
        return "Fizz";
    else if (s % 5 == 0)
        return "Buzz";
    else
    {
        string res = "";
        while (s)
        {
            res = string(1, s % 10 + '0') + res;
            s /= 10;
        }
        return res;
    }
}
int main()
{
    cin >> arr[0];
    cin >> arr[1];
    cin >> arr[2];
    for (int i = 0; i < 3; i++)
        if ('0' <= arr[i][0] && arr[i][0] <= '9')
            hit = i;
    int s = 0;
    for (int i = 0; i < arr[hit].size(); i++)
        s = s * 10 + (arr[hit][i] - '0');
    s += 3 - hit;
    cout << print(s);
    
    return 0;
}
