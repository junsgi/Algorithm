#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int n;
double answer, x[10000], y[10000];
double ccw(double a, double b, double c, double d, double e, double f)
{
	return (a * d + c * f + e * b) - (c * b + e * d + a * f);
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%lf%lf", &x[i], &y[i]);
	for (int i = 2; i < n; i++)
		answer += ccw(x[0], y[0], x[i - 1], y[i - 1], x[i], y[i]) / 2;
	printf("%.1f", abs(answer));
	return 0;
}
