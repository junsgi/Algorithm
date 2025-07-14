#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
struct Node
{
    string value;
    vector<Node*> children;
    Node(string v) : value{ v } {}
    Node() {}
};
int n, m;
vector<vector<string>> arr;
Node* root;
void make_tree(Node*& cur, const vector<string>& list, int depth) 
{

    if (depth == list.size()) return;
    for (Node*& i : cur->children)
        if (i->value == list[depth])
            return make_tree(i, list, depth + 1);
    cur->children.push_back(new Node(list[depth]));
    return make_tree(cur->children.back(), list, depth + 1);
}
int cmp(const Node* x, Node* y) {
    return x->value < y->value;
}
void print(Node*& cur, int depth)
{
    if (depth > 0)
    {
        for (int i = 0; i < depth - 1; i++)
            cout << "--";
        cout << cur->value << '\n';
    }
    sort(cur->children.begin(), cur->children.end(), cmp);
    for (Node*& i : cur->children)
        print(i, depth + 1);
    delete cur;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin >> m;
        arr[i].resize(m);
        for (string& j : arr[i])
            cin >> j;
    }
    sort(arr.begin(), arr.end(), [&](const vector<string>& x, const vector<string>& y) {
        if (x.size() > y.size()) return true;
        if (x.size() < y.size()) return false;
        for (int i = 0; i < x.size(); i++)
        {
            if (x[i] == y[i]) continue;
            return (x[i] < y[i]);
        }
        return false;
    });
    root = new Node("");
    for(vector<string>& i : arr)
        make_tree(root, i, 0);
    print(root, 0);
    return 0;
}