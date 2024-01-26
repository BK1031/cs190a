import sys
from heapq import heappop, heappush

input = sys.stdin.readline

num_nodes, num_edges, exclusion_factor = map(int, input().split())
graph_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]

for _ in range(num_edges):
    start, end, length = map(int, input().split())
    graph_matrix[start - 1][end - 1] = graph_matrix[end - 1][start - 1] = min(graph_matrix[start - 1][end - 1], length)

excluded_nodes = [int(x) - 1 for x in input().split()]
start_node, target_node = map(lambda x: int(x) - 1, input().split())

adjacency_list = [{} for _ in range(num_nodes)]

for i in range(num_nodes):
    for j in range(num_nodes):
        if graph_matrix[i][j] != float('inf'):
            adjacency_list[i][j] = graph_matrix[i][j]

for i in range(num_nodes):
    graph_matrix[i][i] = 0

for k in range(num_nodes):
    for i in range(num_nodes):
        for j in range(num_nodes):
            graph_matrix[i][j] = min(graph_matrix[i][j], graph_matrix[i][k] + graph_matrix[k][j])

path_lengths = graph_matrix[target_node]
node_state = [(float('inf'), float('inf')) for _ in range(num_nodes)]
node_state[start_node] = (0, 0)
priority_queue = [(0, 0, start_node)]

while priority_queue:
    current_ss, current_dd, current_vv = heappop(priority_queue)
    if (current_ss, current_dd) == node_state[current_vv]:
        for next_node in adjacency_list[current_vv]:
            if path_lengths[next_node] and node_state[next_node] > (new := (max((current_dd + adjacency_list[current_vv][next_node]) / path_lengths[next_node], current_ss), current_dd + adjacency_list[current_vv][next_node])):
                node_state[next_node] = new
                heappush(priority_queue, (*new, next_node))

min_path_length = min(160 * node_state[x][0] for x in excluded_nodes)
if min_path_length > 1e9:
    print('IMPOSSIBLE')
else:
    print(min_path_length)
