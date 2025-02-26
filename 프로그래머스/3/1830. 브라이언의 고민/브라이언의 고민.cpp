#include <string>
#include <vector>
#include <iostream>
using namespace std;
int index1(int i, string a)
{
    int res = i;
    while(res + 2 < a.length() && a[res + 2] == a[i])
        res += 2;
    return res;
}
int is1(int begin, int end, string a)
{
    if (begin - 1 < 0 || 'a' <= a[begin - 1]) return 0;
    if (end + 1 >= a.length() || 'a' <= a[end + 1]) return 0;
    return 1;
}
int index2(int i, string a)
{
    int res = a.length() - 1;
    while (res != i and a[res] != a[i]) res--;
    return res;
}
string cut(int i, string a)
{
    return a.substr(0, i);
}
string solution(string sentence) {
    for(char& i : sentence) if (i == ' ') return "invalid";
    string answer = "";
    
    vector<string> filter = {};
    string temp = "";
    int check = 0;
    for(int i = 0 ; i < sentence.length(); i++)
    {
        if (sentence[i] <= 'Z') continue;
        if (check & (1 << (int)(sentence[i] - 'a')))
            return "invalid";
        check |= 1 << (int)(sentence[i] - 'a');
        temp = "";
        int ck1 = index1(i, sentence);
        int ck2 = index2(i, sentence);
        if (ck1 - i == 1 || ck2 - i == 1) return "invalid";
        if (ck1 == ck2 && is1(i, ck1, sentence) && ck1 - i != 2)
        {
            if (i - 1 > 0)
                filter.push_back(cut(i - 1, sentence));
            for(int j = i - 1; j <= ck1 + 1 ; j += 2) temp += sentence[j];
            filter.push_back(temp);
            i = -1;
            if (ck1 + 2 < sentence.length())
                sentence = sentence.substr(ck1 + 2);
            else
                sentence = "";
        }
        else if (i != ck2)
        {
            if (i > 0)
                filter.push_back(cut(i, sentence));
            filter.push_back(sentence.substr(i + 1, ck2 - i - 1));
            i = -1;
            if (ck2 + 1 < sentence.length())
                sentence = sentence.substr(ck2 + 1);
            else
                sentence = "";
        }else
            return "invalid";
    }
    if (sentence.length() > 0) filter.push_back(sentence);
    for(int i = 0 ; i < filter.size() ; i++)
    {
        for(int j = 0 ; j < filter[i].length() ; j++)
        {
            if (filter[i][j] <= 'Z') continue;
            if (check & (1 << (int)(filter[i][j] - 'a')))
                return "invalid";
            check |= 1 << (int)(filter[i][j] - 'a');
            
            if (j - 1 > 0)
                answer += cut(j - 1, filter[i]) + " ";
            
            temp = "";
            int ck1 = index1(j, filter[i]);
            if (!is1(j, ck1, filter[i])) return "invalid";
            for(int k = j - 1; k <= ck1 + 1 ; k += 2) temp += filter[i][k];
            answer += temp + " ";
            j = -1;
            if (ck1 + 2 < filter[i].length())
                filter[i] = filter[i].substr(ck1 + 2);
            else
                filter[i] = "";
        }
        for(char& j: filter[i])
            if ('a' <= j) return "invalid";
        if(filter[i].size() > 0)
            answer += filter[i] + " ";
    }
    return answer.substr(0, answer.length() - 1);
}