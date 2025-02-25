#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    int c[] = {6, 6, 5, 4, 3, 2, 1}; 
    int zero = 0;
    int right = 0;
    for(int i = 0 ; i < 6 ; i++)
    {
        if (lottos[i] == 0)
            zero++;
        else
        {
            for(int j = 0 ; j < 6; j++)
                if (lottos[i] == win_nums[j])
                {
                    right++;
                    break;
                }
        }
    }
    return {c[right + zero], c[right]};
}