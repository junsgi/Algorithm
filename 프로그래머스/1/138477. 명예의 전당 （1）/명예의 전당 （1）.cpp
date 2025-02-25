#include <string>
#include <vector>

using namespace std;
void up(int idx, int* heap);
void down(int idx, int* heap);
int len;
vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    len = 0;
    int* heap = new int[score.size() + 1] {};
    for(int& i : score)
    {
        if (len != k)
        {
            heap[++len] = i;
            up(len, heap);
        }
        else
        {
            if (heap[1] < i) 
            {
                heap[1] = heap[len--];
                down(1, heap);
                
                heap[++len] = i;
                up(len, heap);
            }
            
        }
        answer.push_back(heap[1]);
    }
    return answer;
}
void up(int idx, int* heap)
{
    if (idx / 2 == 0) return;
    if (heap[idx] < heap[idx / 2])
    {
        int tmp = heap[idx]; heap[idx] = heap[idx / 2]; heap[idx / 2] = tmp;
        up(idx / 2, heap);
    }
}
void down(int idx, int* heap)
{
    int child = idx * 2;
    if (child > len) return;
    if (child + 1 <= len && heap[child] > heap[child + 1])
        child++;
    if (heap[idx] > heap[child])
    {
        int tmp = heap[idx]; heap[idx] = heap[child]; heap[child] = tmp;
        down(child, heap);
    }
}