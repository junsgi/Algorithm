#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int n;
string DP[101] = { "0", "0", "1", "7", "4", "2", "6", "8"};
void solution()
{
	for (int i = 8; i <= 100; i++)
	{
		int left = 2, right = i - 2;
		long long res = 8888888888888888;
		string ans = "";
		while (left <= right)
		{
			long long n1 = stoll(DP[left] + (right == 6 ? "0" : DP[right]));
			if (n1 < res)
			{
				res = n1;
				ans = DP[left] + (right == 6 ? "0" : DP[right]);
			}

			long long n2 = stoll(DP[right] + (left == 6 ? "0" : DP[left]));
			if (n2 < res)
			{
				res = n2;
				ans = DP[right] + (left == 6 ? "0" : DP[left]);
			}
			left++; right--;
		}
		DP[i] = ans;
	}
}
string MAX(int n)
{
	string res = (n & 1) ? "7" : "1";
	while (3 < n)
	{
		res += "1";
		n -= 2;
	}
	return res;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	solution();
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int t;
		cin >> t;
		cout << DP[t] << " " << MAX(t) << '\n';
	}
	return 0;
}
