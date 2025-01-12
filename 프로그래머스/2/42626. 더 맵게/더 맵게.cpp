#include <string>
#include <vector>

using namespace std;
int heap[1'000'001], idx = 0, tmp;
void up(int i)
{
    if (i / 2 <= 0) return;
    if (heap[i] < heap[i / 2])
    {
        tmp = heap[i]; heap[i] = heap[i / 2]; heap[i / 2] = tmp;
        up(i / 2);
    }
}
void down(int i)
{
    int c = i * 2;
    if (c > idx) return;
    if (c + 1 <= idx && heap[c] > heap[c + 1])
        c++;
    if (heap[i] > heap[c])
    {
        tmp = heap[i]; heap[i] = heap[c]; heap[c] = tmp;
        down(c);
    }
}
int solution(vector<int> scoville, int K) {
    int answer = 0;
    for(auto i : scoville)
    {
        heap[++idx] = i;
        up(idx);
    }
    while (idx > 1 && heap[1] < K)
    {
        int n1 = heap[1];
        heap[1] = heap[idx--];
        down(1);
        int n2 = heap[1];
        heap[1] = heap[idx--];
        down(1);
        
        answer++;
        heap[++idx] = n1 + n2 * 2;
        up(idx);
    }
    if (idx == 0 || heap[1] < K)
        return -1;
    return answer;
}