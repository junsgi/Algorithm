#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#include<set>
using namespace std;
int n, m;
char com[10];
set<int> s;
int main()
{
	scanf("%d", &n);
	while (n--)
	{
		scanf("%s", com);
		if (!strcmp(com, "add"))
		{
			scanf("%d", &m);
			s.insert(m);
		}
		else if (!strcmp(com, "all"))
		{
			for (int i = 1; i <= 20; i++)
				s.insert(i);
		}
		else if (!strcmp(com, "remove"))
		{
			scanf("%d", &m);
			s.erase(m);
		}
		else if (!strcmp(com, "check"))
		{
			scanf("%d", &m);
			printf("%d\n", s.find(m) != s.end());
		}
		else if (!strcmp(com, "toggle"))
		{
			scanf("%d", &m);
			if (s.find(m) == s.end())
				s.insert(m);
			else
				s.erase(m);
		}
		else
			s.clear();
	}
	return 0;
}