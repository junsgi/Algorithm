#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#include <tuple>
#include <queue>
#include <unordered_map>
using namespace std;
using ui = unsigned int;
class BitArray
{
public:
    BitArray()
    {
        arr = 0;
        sz = 0;
    }
    void push(int n) 
    { 
        arr = (arr << 4) + n; 
        sz++;
    }
    void swap(int l, int r)
    {
        ui sl = shift(l), sr = shift(r);
        int left = operator[](l);
        int right = operator[](r);

        arr &= ~((MASK << sl) | (MASK << sr));
        arr |= (left << sr) | (right << sl);
    }
    int operator[](int idx) const
    {
        ui s = shift(idx);
        return (arr >> s) & MASK;
    }
    ui shift(int idx) const { return 4 * (sz - 1 - idx); }
    int size() const { return sz; }
    ui get() { return arr; }
private:
    ui arr;
    static const ui MASK = (1 << 4) - 1;
    int sz;
};
struct Node 
{ 
    BitArray obj;
    int cost;
    bool operator>(const Node& other) const
    {
        return cost > other.cost;
    }
};
int n, m;
BitArray arr;
vector<tuple<int, int, int>> info;
unordered_map<ui, int> map;
priority_queue<Node, vector<Node>, greater<Node>> heap;
int isSorted(BitArray& x)
{
    for (int i = 1; i < n; i++)
        if (x[i - 1] > x[i]) return 0;
    return 1;
}
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &m);
        arr.push(m);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c); a--; b--;
        info.push_back({ a, b, c });
    }
    map[arr.get()] = 0;
    heap.push({ arr, 0 });
    while (!heap.empty())
    {
        Node cur = heap.top(); heap.pop();
        BitArray obj = cur.obj;
        if (map[obj.get()] < cur.cost) continue;
        if (isSorted(obj))
        {
            printf("%d", cur.cost);
            return 0;
        }
        
        for (const auto& [st, ed, cost] : info)
        {
            obj.swap(st, ed);
            if (map.find(obj.get()) == map.end() || map[obj.get()] > cur.cost + cost)
            {
                map[obj.get()] = cur.cost + cost;
                heap.push({ obj, cur.cost + cost });
            }
            obj.swap(ed, st);
        }
    }
    printf("-1");
    return 0;
}