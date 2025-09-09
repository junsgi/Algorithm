#include <iostream>
#include <string>
#include <vector>
using namespace std;
string text;
int solution(string pattern)
{
	int psize = pattern.size();
	vector<int> res(psize, 0);
	int x = 0, cnt = 0;
	for (int i = 1; i < psize; ++i)
	{
		while (x > 0 && pattern[x] != pattern[i])
			x = res[x - 1];
		if (pattern[x] == pattern[i])
			res[i] = ++x;
		cnt = max(cnt, res[i]);
	}
	return cnt;
}

int main() 
{
	cin >> text;
	int ans = 0;
	for (int i = 0; i < text.length(); ++i)
		ans = max(ans, solution(text.substr(i)));
	cout << ans;
	return 0;
}