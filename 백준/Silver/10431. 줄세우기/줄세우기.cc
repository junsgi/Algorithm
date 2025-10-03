#include <iostream>
using namespace std;
int n, c, arr[20];
int main()
{
	cin.tie(nullptr); cout.tie(nullptr);
	ios_base::sync_with_stdio(false);
	cin >> n;
	while (n--)
	{
		cin >> c;
		for (int i = 0; i < 20; ++i) cin >> arr[i];
		int ans = 0;
		for (int i = 1; i < 20; ++i)
		{
			for (int j = i - 1; j >= 0; --j)
			{
				if (arr[j] > arr[j + 1])
				{
					++ans;
					swap(arr[j], arr[j + 1]);
				}
				else break;
			}
		}
		cout << c << ' ' << ans << '\n';
	}
	return 0;
}
