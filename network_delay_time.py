class PriorityQueue:
    def __init__(self, N):
        self.q = [[None, i] for i in range(1, N + 1)]
        self.nodeidxs = {i: i - 1 for i in range(1, N + 1)}

    def bubble_up(self, node, wt):
        idx = self.nodeidxs[node]
        cur_wt = self.q[idx][0]
        if cur_wt is None or wt < cur_wt:
            self.q[idx][0] = wt

        par_idx = idx // 2 if idx % 2 else idx // 2 - 1
        while par_idx >= 0 and (self.q[par_idx][0] is None or self.q[par_idx][0] > wt):
            self.nodeidxs[node], self.nodeidxs[self.q[par_idx][1]] = par_idx, idx # noqa
            self.q[idx], self.q[par_idx] = self.q[par_idx], self.q[idx]
            idx = par_idx
            par_idx = idx // 2 if idx % 2 else idx // 2 - 1
            
    def bubble_down(self, idx=0, l_idx=1, r_idx=2):
        while True:
            l_idx = idx * 2 + 1
            r_idx = idx * 2 + 2
            if l_idx >= len(self.q):
                return
            
            less = l_idx
            
            if r_idx < len(self.q) and self.q[r_idx][0] is not None and self.q[r_idx][0] < self.q[l_idx][0]:
                less = r_idx
                
            if self.q[less][0] is None:
                return
            
            if self.q[idx][0] > self.q[less][0]:
                self.nodeidxs[self.q[idx][1]] = less
                self.nodeidxs[self.q[less][1]] = idx
                self.q[idx], self.q[less] = self.q[less], self.q[idx]
                idx = less
            else:
                break

    def get_min(self):
        self.q[0], self.q[-1] = self.q[-1], self.q[0]
        self.nodeidxs[self.q[0][1]], self.nodeidxs[self.q[-1][1]] = \
            self.nodeidxs[self.q[-1][1]], self.nodeidxs[self.q[0][1]]
        mini = self.q.pop()
        if len(self.q) > 1:
            self.bubble_down()
        return mini


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        visited = {}

        # Create edges dict
        edges = {i: {} for i in range(1, N + 1)}
        for time in times:
                edges[time[0]][time[1]] = time[2]

        # Initialize Priority Queue
        q = PriorityQueue(N)
        q.bubble_up(K, 0)

        while len(q.q) > 0:
            closest = q.get_min()
            visited[closest[1]] = closest[0]
            for neighbor, wt in edges[closest[1]].items():
                if neighbor not in visited.keys():
                    q.bubble_up(neighbor, closest[0] + wt)
                    
        return closest[0] if closest[0] is not None else -1
