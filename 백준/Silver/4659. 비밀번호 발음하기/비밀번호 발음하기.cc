#include<iostream>
#include<string>
using namespace std;
int isGather(char& c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
void solution(string& s)
{
	int ck = 0;
	for (int i = 0; i < s.length(); ++i)
	{
		char& c = s[i];
		if (isGather(c)) ck = 1;
		if (i > 1 && (isGather(s[i]) && isGather(s[i - 1]) && isGather(s[i - 2]) || !isGather(s[i]) && !isGather(s[i - 1]) && !isGather(s[i - 2])))
		{
			cout << '<' << s << '>' << " is not acceptable.\n";
			return;
		}
		if (i > 0 && c != 'e' && c != 'o' && c == s[i - 1])
		{
			cout << '<' << s << '>' << " is not acceptable.\n";
			return;
		}
	}
	if (!ck)
		cout << '<' << s << '>' << " is not acceptable.\n";
	else
		cout << '<' << s << '>' << " is acceptable.\n";
}
int main()
{
	cin.tie(nullptr)->sync_with_stdio(false);
	cout.tie(nullptr)->sync_with_stdio(false);
	string s;
	while (1)
	{
		cin >> s;
		if (s == "end") break;
		solution(s);
	}
	return 0;
}