#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int freq[241];
int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    for(int i = 0 ; i < (int)people.size() ; i++) freq[people[i]]++;
    for(int i = 0 ; i < (int)people.size() ; i++)
    {
        if (!freq[people[i]])
            continue;
        answer++;
        freq[people[i]]--;
        for(int j = limit - people[i]; j > 0 ; j--)
        {
            if (freq[j] && j + people[i] <= limit)
            {
                freq[j]--;
                break;
            }
        }
    }
        
    return answer;
}