#include <string>
#include <vector>

using namespace std;
string temp[50];
void Sort(int left, int right, vector<string>& arr, int n)
{
    int mid = (left + right) / 2;
    int l = left;
    int r = mid + 1;
    int idx = 0;
    while (l <= mid && r <= right)
    {
        if (arr[l][n] < arr[r][n] || arr[l][n] == arr[r][n] && arr[l] < arr[r])
            temp[idx++] = arr[l++];
        else
            temp[idx++] = arr[r++];
    }
    while (l <= mid) temp[idx++] = arr[l++];
    while (r <= right) temp[idx++] = arr[r++];
    for(int i = 0 ; i < idx ; i++)
        arr[left + i] = temp[i];
}
void merge(int left, int right, vector<string>& arr, int n)
{
    if (left >= right) return;
    int mid = (left + right) / 2;
    merge(left, mid, arr, n);
    merge(mid + 1, right, arr, n);
    Sort(left, right, arr, n);
}
vector<string> solution(vector<string> strings, int n) {
    merge(0, strings.size() - 1, strings, n);
    return strings;
}