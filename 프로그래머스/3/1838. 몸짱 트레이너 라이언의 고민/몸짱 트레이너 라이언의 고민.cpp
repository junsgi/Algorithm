#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
typedef pair<int, int> pii;
vector<pii> arr;
int c(pii x, pii y)
{
    return x.first < y.first || (x.first == y.first && x.second > y.second);
}
int solution(int n, int m, vector<vector<int>> timetable) {
    if (!m) return 0;
    arr.clear();
    for(auto& i : timetable)
    {
        arr.push_back(make_pair(i[0], 1));
        arr.push_back(make_pair(i[1], -1));
    }
    sort(arr.begin(), arr.end(), c);
    int s = 0, ck = 0;
    for(int i = 0; i < arr.size() ; i++)
    {
        s += arr[i].second;
        ck = max(ck, s);
    }
    if (ck <= 1) return 0;
    int left = 1, right = (n - 1) * 2;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        for(int a = 0 ; a < n ; a++)
        {
            for(int b = 0 ; b < n ; b++)
            {
                if (a && b) continue;
                arr.clear();
                arr.push_back(make_pair(a, b));
                for(int x = 0; x < n ; x++)
                {
                    for(int y = 0; y < n ; y++)
                    {
                        if (abs(arr[arr.size() - 1].first - x) + abs(arr[arr.size() - 1].second - y) < mid) continue;
                        bool flag = true;
                        for(auto& z : arr)
                        {
                            if (abs(x - z.first) + abs(y - z.second) < mid)
                            {
                                flag = false;
                                break;
                            }
                        }
                        if(flag)
                            arr.push_back(make_pair(x, y));
                    }
                }
                if ((int)arr.size() >= ck) break;
            } // b
            if ((int)arr.size() >= ck) break;
        } // a
        
        if ((int)arr.size() < ck)
            right = mid - 1;
        else
            left = mid + 1;
    } // binary
    return right;
}
