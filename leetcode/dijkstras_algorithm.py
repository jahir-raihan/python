dic = {}

times = [[1, 2, 1], [2, 1, 3]]

for i in times:
    if i[0] in dic:
        dic[i[0]][i[1]] = i[2]
        if i[1] in dic:
            dic[i[1]][i[0]] = i[2]
        else:
            dic[i[1]] = {i[0]: i[2]}

    else:
        dic[i[0]] = {i[1]: i[2]}
        dic[i[1]] = {i[0]: i[2]}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    track_predecessors = {}
    unseen_nodes = graph
    inf = 99999999
    path = []   # Trace our node the source node

    for node in unseen_nodes:
        """This loop initially marks all vertex distance as infinity."""
        shortest_distance[node] = inf

    shortest_distance[start] = 0

    while unseen_nodes:
        """Looping Through the graph"""
        break_out = False
        """Start -> this part of code will be optimized"""

        min_distance_node = None

        """At this point we are searching for smallest weighted  neighbor"""
        for node in unseen_nodes:

            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:

                min_distance_node = node

        path_options = graph[min_distance_node].items()

        """End -> This part of code will be optimized. """

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessors[child_node] = min_distance_node

                """We can also optimize at here too.By adding an additional condition.
                   If the child node is goal node we can just break out of the loop."""
                # if child_node == goal:
                #     break_out = True
                #     break

        unseen_nodes.pop(min_distance_node)
        if break_out:
            break

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = track_predecessors[current_node]
        except KeyError:
            break
    path.insert(0, start)
    if shortest_distance[goal] != inf:
        print('Shortest distance is', shortest_distance[goal])
        print('Optimal path is', path)


dijkstra(dic, 2, 2)