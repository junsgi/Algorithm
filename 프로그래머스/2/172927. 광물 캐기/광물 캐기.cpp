#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int answer = 0x7fffffff;
void DFS(int c, vector<int> ref, vector<int> picks, vector<int> minerals)
{
    if (c == 0)
    {
        int t = 0;
        for(int i = 0 ; i < picks.size() ; i++)
        {
            int flag = 0;
            int pick = picks[i];
            for(int j = i * 5; j < i * 5 + 5 ; j++)
            {
                if (j >= minerals.size()) 
                {
                    flag = 1;
                    break;
                }
                if (pick - minerals[j] >= 0)
                    t++;
                else
                {
                    int temp = 1;
                    for(int k = 0 ; k < minerals[j] - pick ; k++)
                        temp *= 5;
                    t += temp;
                    if (t >= answer) return;
                }
            }
            if (flag) break;
        }
        answer = min(answer, t);
        return;
    }
    for(int i = 0 ; i < 3 ; i++)
    {
        if (ref[i] == 0) continue;
        picks.push_back(2 - i);
        ref[i]--;
        DFS(c - 1, ref, picks, minerals);
        picks.pop_back();
        ref[i]++;
    }
}
int solution(vector<int> picks, vector<string> minerals) {
    vector<int> arr = {};
    for(auto i : minerals)
    {
        if (!i.compare("diamond")) arr.push_back(2);
        else if (!i.compare("iron")) arr.push_back(1);
        else arr.push_back(0);
    }
    int c = 0;
    for(int i = 0 ; i < 3; i ++) c += picks[i];
    DFS(c, picks, {}, arr);
    return answer;
}