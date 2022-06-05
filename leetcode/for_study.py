import heapq
from collections import defaultdict

edg_list = [[1, 2, 1], [2, 1, 3]]


class Solution:
    
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)
        for src, dest, cost in times:
            graph[src].append((dest, cost))

        queue = [(0, k)]
        visited = {}
        max_cost = 0
        while queue:
            cost, node = heapq.heappop(queue)
            if node not in visited:
                visited[node] = True
                max_cost = max(max_cost, cost)
                for neighbour, new_cost in graph[node]:
                    if neighbour not in visited:
                        heapq.heappush(queue, (cost + new_cost, neighbour))

        if len(visited) == n:
            return max_cost
        else:
            return -1

var = Solution()
var.networkDelayTime(edg_list, 2, 2)