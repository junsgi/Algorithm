#include<iostream>
#include<string>
#include<unordered_set>
using namespace std;
int n;
char m;
unordered_set<string> set;
int key()
{
	if (m == 'Y') return 2;
	if (m == 'F') return 3;
	return 4;
}
int main()
{
	cin.tie(nullptr)->sync_with_stdio(false);
	cout.tie(nullptr)->sync_with_stdio(false);
	cin >> n >> m;
	string s;
	while (n--)
	{
		cin >> s;
		set.insert(s);
	}
	cout << set.size() / (key() - 1);
	return 0;
}