#pragma warning(disable:4996)
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std; typedef pair<int, int> pii;
long long DP[360001];
int splitAndSum(string t)
{
    int hour = stoi(t.substr(0, 2));
    int minute = stoi(t.substr(3, 5));
    int sec = stoi(t.substr(6, 8));
    return hour * 3600 + minute * 60 + sec;
}
string rollback(int t)
{
    string hour = to_string(t / 3600);
    if (hour.size() == 1){
        hour = "0" + hour;
    }
    t %= 3600;
    string minute = to_string(t / 60);
    if (minute.size() == 1){
        minute = "0" + minute;
    }
    t %= 60;
    string sec = to_string(t);
    if (sec.size() == 1){
        sec = "0" + sec;
    }
    return hour + ":" + minute + ":" + sec;
}
pii get(string t)
{
    int start = splitAndSum(t.substr(0, 8));
    int end = splitAndSum(t.substr(9, 17));
    return make_pair(start, end);
}
string solution(string play_time, string adv_time, vector<string> logs)
{
    int playTime = splitAndSum(play_time);
    for (int i = 0; i < logs.size(); i++)
    {
        pii result = get(logs[i]);
        DP[result.first]++;
        DP[result.second]--;
    }
    for (int i = 1; i <= playTime ; i++)
        DP[i] += DP[i - 1];
    for (int i = 1; i <= playTime ; i++)
        DP[i] += DP[i - 1];
    int advT = splitAndSum(adv_time) - 1;
    int ansMin = 0;
    long long ansMax = DP[advT];
    for(int ed = advT; ed < playTime ; ed++)
    {
        int i = ed - advT - 1;
        long long temp = 0L;
        if (i < 0) temp = DP[ed];
        else temp = DP[ed] - DP[i];
        
        if (ansMax < temp)
        {
            ansMax = temp;
            ansMin = ed - advT;
        }
    }
    return rollback(ansMin);
}
