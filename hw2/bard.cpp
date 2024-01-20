#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    std::unordered_map<int, std::unordered_set<int>> map;
    for (int i = 1; i <= n; ++i) {
        map[i] = std::unordered_set<int>();
    }

    int m;
    std::cin >> m;

    int bardKnows = 0;
    for (int i = 0; i < m; ++i) {
        int k;
        std::cin >> k;

        bool bard = false;
        std::unordered_set<int> villageSet;
        for (int j = 0; j < k; ++j) {
            int v;
            std::cin >> v;
            villageSet.insert(v);
            if (v == 1)
                bard = true;
        }

        if (bard) {
            ++bardKnows;
            for (int v : villageSet) {
                map[v].insert(bardKnows);
            }
        } else {
            std::unordered_set<int> all;
            for (int v : villageSet) {
                all.insert(map[v].begin(), map[v].end());
            }
            for (int v : villageSet) {
                map[v].insert(all.begin(), all.end());
            }
        }
    }

    int max = map[1].size();
    for (int i = 1; i <= n; ++i) {
        if (map[i].size() == max) {
            std::cout << i << std::endl;
        }
    }

    return 0;
}
