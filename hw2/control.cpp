#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int parent[500001], set_size[500001];

int find(int v) {
    return parent[v] == v ? v : parent[v] = find(parent[v]);
}

void union_sets(int a, int b) {
    int ra = find(a), rb = find(b);
    if (ra == rb) return;
    if (set_size[ra] < set_size[rb]) swap(ra, rb);
    parent[rb] = ra;
    set_size[ra] += set_size[rb];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i = 0; i < 500001; i++) {
        parent[i] = i;
        set_size[i] = 1;
    }
    
    int n, m, count = 0, x;
    cin >> n;
    while (n--) {
        cin >> m;
        unordered_set<int> roots;
        vector<int> ingredients(m);
        for (int i = 0; i < m; i++) {
            cin >> ingredients[i];
            roots.insert(find(ingredients[i]));
        }

        int total = 0;
        for (auto &r : roots) total += set_size[find(r)];

        if (total == m) {
            count++;
            for (int i = 1; i < m; i++) union_sets(ingredients[0], ingredients[i]);
        }
    }
    cout << count;
    return 0;
}
