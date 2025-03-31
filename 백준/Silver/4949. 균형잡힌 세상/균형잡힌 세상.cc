#include<iostream>
#include<string>
using namespace std;
int top;
char stk[101];
string str;
int main()
{
	while (1)
	{
		getline(cin, str);
		if (str == ".")
			break;
		top = -1;
		for (int i = 0; i < str.size(); i++)
		{
			if (str[i] != '(' && str[i] != ')' && str[i] != '[' && str[i] != ']') continue;

			if (str[i] == '(' || str[i] == '[')
				stk[++top] = str[i];
			else
			{
				if (top == -1 || (str[i] == ')' && stk[top] == '[') || (str[i] == ']' && stk[top] == '('))
				{
					top = 0;
					break;
				}
				top--;
			}
		}
		if (top != -1)
			cout << "no\n";
		else
			cout << "yes\n";

	}
	return 0;
}
