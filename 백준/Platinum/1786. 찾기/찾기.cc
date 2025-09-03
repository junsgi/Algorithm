#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> kmp_search(const string& T, const string& P) {
    int n = T.size(), m = P.size();
    vector<int> lps(m), result;

    // 1. lps 배열 만들기
    for (int i = 1, len = 0; i < m; ) {
        if (P[i] == P[len]) lps[i++] = ++len;
        else if (len) len = lps[len - 1];
        else lps[i++] = 0;
    }

    // 2. 본문 탐색
    for (int i = 0, j = 0; i < n; ) {
        if (T[i] == P[j]) { i++; j++; }
        if (j == m) {
            result.push_back(i - j); // 패턴 발견 (0-based 위치)
            j = lps[j - 1];
        }
        else if (i < n && T[i] != P[j]) {
            if (j) j = lps[j - 1];
            else i++;
        }
    }
    return result;
}

int main() {
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    string T, P;
    getline(cin, T);
    getline(cin, P);

    auto matches = kmp_search(T, P);
    cout << matches.size() << "\n";
    for (int pos : matches) cout << pos + 1 << " "; // 1-based 출력
}