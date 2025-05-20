#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    int sx = 100, sy = 100, ex = 0, ey = 0;
    for(int i = 0 ; i < wallpaper.size(); i++)
    {
        for(int j = 0 ; j < wallpaper[i].size(); j++)
        {
            if (wallpaper[i][j] == '.') continue;
            sx = min(sx, i);
            sy = min(sy, j);
            ex = max(ex, i);
            ey = max(ey, j);
        }
    }
    return {sx, sy, ex + 1, ey + 1};
}