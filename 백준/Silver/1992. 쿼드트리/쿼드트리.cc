#include<iostream>
#include<string>
using namespace std;
short n;
string matrix[64];
string func(short x, short y, short z)
{
	if (z == 1) 
		return string(1, matrix[x][y]);
	string a = func(x, y, z / 2);
	string b = func(x, y + z / 2, z / 2);
	string c = func(x + z / 2, y, z / 2);
	string d = func(x + z / 2, y + z / 2, z / 2);
	if (a.size() == 1 && a == b && b == c && c == d)
		return a;
	return "(" + a + b + c + d + ")";
}
int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> matrix[i];
	cout << func(0, 0, n);
	return 0;
}