#pragma warning(disable:4996)
#include<stdio.h>
int n, mat[100][100];
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n * n; i++) scanf("%d", &mat[i / n][i % n]);
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (mat[i][k] && mat[k][j])
                    mat[i][j] = 1;
            }
        }

    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%d ", mat[i][j]);
        printf("\n");
    }
    return 0;
}