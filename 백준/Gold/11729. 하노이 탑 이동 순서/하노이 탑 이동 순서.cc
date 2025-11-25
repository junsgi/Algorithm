#include<iostream>
#define fastio ios_base::sync_with_stdio(false);cout.tie(nullptr);cin.tie(nullptr);
using namespace std;
int n;
void hanoi(int st, int ed, int num)
{
	if (num == 0) return;
	hanoi(st, 6 - (st + ed), num - 1);
	cout << st << ' ' << ed << '\n';
	hanoi(6 - (st + ed), ed, num - 1);
}
int main()
{
	fastio;
	cin >> n;
	cout << (1 << n) - 1 << '\n';
	hanoi(1, 3, n);
	return 0;
}