#include <iostream>
#include <vector>
#include <queue>

using namespace std;
typedef long long ll;

struct Edge {
    ll weight, destination;

    Edge(ll w, ll d) : weight(w), destination(d) {}
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ll test_cases;
    cin >> test_cases;

    while (test_cases--) {
        ll nodes, edges, length, start_nodes;
        cin >> nodes >> edges >> length >> start_nodes;
        vector<bool> visited(nodes, false);
        vector<ll> starting_nodes;
        for (ll i = 0; i < start_nodes; i++) {
            ll node;
            cin >> node;
            node--;

            visited[node] = true;
            starting_nodes.push_back(node);
        }

        vector<vector<Edge>> adj_list(nodes);
        for (ll i = 0; i < edges; i++) {
            ll node1, node2, weight;
            cin >> node1 >> node2 >> weight;
            node1--;
            node2--;

            adj_list[node1].emplace_back(weight + length, node2);
            adj_list[node2].emplace_back(weight + length, node1);
        }

        priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> pq;
        for (auto start_node : starting_nodes) {
            for (auto &edge : adj_list[start_node]) {
                pq.push({edge.weight, edge.destination});
            }
        }

        ll total_cost = 0;
        while (!pq.empty()) {
            ll current_node = pq.top().second;
            ll current_distance = pq.top().first;
            pq.pop();

            if (visited[current_node]) {
                continue;
            }
            visited[current_node] = true;
            total_cost += current_distance;
            for (auto &edge : adj_list[current_node]) {
                pq.push({edge.weight, edge.destination});
            }
        }

        cout << total_cost << endl;
    }

    return 0;
}
