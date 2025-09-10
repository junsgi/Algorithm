#include <iostream>
#include <string>
#include <vector>
using namespace std;
string text;
int solution(string& pattern)
{
	int psize = pattern.length();
	vector<int> res(psize, 0);
	int x = 0;
	for (int i = 1; i < psize; ++i)
	{
		while (x > 0 && pattern[x] != pattern[i])
			x = res[x - 1];
		if (pattern[x] == pattern[i])
			res[i] = ++x;
	}
	return res.back();
}

int main() 
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	while (1) 
	{
		cin >> text;
		if (text == ".") break;
		if (text.length() == 1)
		{
			cout << 1 << '\n';
			continue;
		}
		int cnt = solution(text);
		if (!cnt || text.length() % (text.length() - cnt) != 0) cout << 1 << '\n';
		else cout << text.length() / (text.length() - cnt) << '\n';
	}
	return 0;
}