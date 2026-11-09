# LeetCode 1606. Find Servers That Handled Most Number of Requests
# Difficulty: Hard | Daily Challenge, 2026-11-09
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
#
# Idea: a min-heap holds busy servers by finish time, so servers that
# free up by the current arrival time go back to the available pool.
# The available pool is a Fenwick tree (1 = free), which finds the
# next free server at or after i % k in O(log k), wrapping to the
# smallest free server when there is none. Count requests per server
# and return every server with the maximum count.

import heapq

class BIT:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)
        for i in range(1, n + 1):
            self.t[i] = i & -i  # all servers free at the start

    def add(self, i, d):  # 0-indexed
        i += 1
        while i <= self.n:
            self.t[i] += d
            i += i & -i

    def sum(self, i):  # sum of [0, i)
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s

    def find_kth(self, k):  # 1-indexed k, smallest index with prefix sum >= k
        idx = 0
        bit = 1 << self.n.bit_length()
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.t[nxt] < k:
                k -= self.t[nxt]
                idx = nxt
            bit >>= 1
        return idx  # 0-indexed position


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        bit = BIT(k)
        busy = []  # (finish_time, server)
        count = [0] * k
        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, s = heapq.heappop(busy)
                bit.add(s, 1)
            total = bit.sum(k)
            if total == 0:
                continue  # every server busy, request dropped
            start = i % k
            before = bit.sum(start)  # free servers in [0, start)
            if total - before > 0:
                s = bit.find_kth(before + 1)
            else:
                s = bit.find_kth(1)  # wrap around to the smallest free server
            bit.add(s, -1)
            count[s] += 1
            heapq.heappush(busy, (a + l, s))
        m = max(count)
        return [i for i, c in enumerate(count) if c == m]
