#pragma warning(disable:4996)
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int MOD = 20170805;
int DP[2][500][500];
int inRange(int x, int y, vector<vector<int>>& graph)
{
    return 0 <= x && x < graph.size() && 0 <= y && y < graph[0].size();
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < m; k++)
                DP[i][j][k] = 0;
    // 0 : 왼쪽에서 오른쪽
    // 1 : 위에서 아래
    DP[0][0][0] = DP[1][0][0] = 1;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 && j == 0) continue;
            if (city_map[i][j] == 1) continue;
            int lx = i, ly = j - 1;
            int ux = i - 1, uy = j;
            int cnt = 0;
            if (city_map[i][j] == 0)
            {
                if (inRange(lx, ly, city_map))
                    cnt += DP[0][lx][ly];
                if (inRange(ux, uy, city_map))
                    cnt = (cnt + DP[1][ux][uy]) % MOD;
                DP[0][i][j] = DP[1][i][j] = cnt;
            }
            else
            {
                if (inRange(lx, ly, city_map))
                    DP[0][i][j] = (DP[0][i][j] + DP[0][lx][ly]) % MOD;
                if (inRange(ux, uy, city_map))
                    DP[1][i][j] = (DP[1][i][j] + DP[1][ux][uy]) % MOD;
            }
        }
    }
    return DP[0][m - 1][n - 1];
}