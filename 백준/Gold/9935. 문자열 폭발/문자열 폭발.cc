#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
int len;
char str[1000011], ex[40], stk[1000111];
int cmp()
{
    if (len + 1 < strlen(ex)) return 0;
    return strcmp(stk + (len - strlen(ex) + 1), ex) == 0;
}
int main()
{
    scanf("%s", str);
    scanf("%s", ex);
    len = -1;
    for (int i = 0; str[i]; i++)
    {
        while (cmp())
        {
            len -= (int)strlen(ex);
            for (int j = len + 1; j < len + 1 + strlen(ex); j++) stk[j] = '\0';
        }
        stk[++len] = str[i];
    }
    while (cmp())
    {
        len -= (int)strlen(ex);
        for (int j = len + 1; j < len + 1 + strlen(ex); j++) stk[j] = '\0';
    }
    if (len <= -1) printf("FRULA");
    else printf("%s", stk);
    return 0;
}
