#include <iostream>
#include <vector>
using namespace std;
constexpr int m = 360'000;
int n, tmp, arr1[(m << 1) | 1], arr2[m + 1];
vector<int> make_lps()
{
	vector<int> res(m + 1, 0);
	int x = 0;
	for (int i = 1; i < m + 1; ++i)
	{
		while (x > 0 && arr2[x] != arr2[i])
			x = res[x - 1];
		if (arr2[x] == arr2[i])
			res[i] = ++x;
	}
	return res;
}
void kmp()
{
	vector<int> lps = make_lps();
	int pt = 0, pp = 0;
	while(pt < ((m << 1) | 1))
	{
		if (arr1[pt] == arr2[pp])
		{
			++pt; ++pp;
			if (pp == m)
			{
				cout << "possible";
				return;
			}
		}
		else if (pp) pp = lps[pp - 1];
		else ++pt;
	}
	cout << "impossible";
	return;
}
int main() 
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> tmp;
		arr1[tmp] = 1;
		arr1[m + tmp] = 1;
	}
	for (int i = 0; i < n; ++i)
	{
		cin >> tmp;
		arr2[tmp] = 1;
	}
	kmp();
	return 0;
}