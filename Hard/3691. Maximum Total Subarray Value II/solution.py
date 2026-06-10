from typing import List
import heapq

class SparseTable:
    def __init__(self, arr: List[int]):
        n = len(arr)
        self.n = n
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        self.st_max = [[0] * (self.log[n] + 1) for _ in range(n)]
        self.st_min = [[0] * (self.log[n] + 1) for _ in range(n)]

        for i in range(n):
            self.st_max[i][0] = self.st_min[i][0] = arr[i]

        for j in range(1, self.log[n] + 1):
            for i in range(n - (1 << j) + 1):
                self.st_max[i][j] = max(self.st_max[i][j-1], 
                                       self.st_max[i + (1 << (j-1))][j-1])
                self.st_min[i][j] = min(self.st_min[i][j-1], 
                                       self.st_min[i + (1 << (j-1))][j-1])

    def query_max(self, L: int, R: int) -> int:
        k = self.log[R - L + 1]
        return max(self.st_max[L][k], self.st_max[R - (1 << k) + 1][k])

    def query_min(self, L: int, R: int) -> int:
        k = self.log[R - L + 1]
        return min(self.st_min[L][k], self.st_min[R - (1 << k) + 1][k])


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0

        st = SparseTable(nums)
        
        pq = []
        for left in range(n):
            if left < n: 
                val = st.query_max(left, n-1) - st.query_min(left, n-1)
                heapq.heappush(pq, (-val, left, n-1))

        ans = 0
        for _ in range(k):
            if not pq:
                break
            neg_val, left, right = heapq.heappop(pq)
            ans -= neg_val

            if right > left:
                new_val = st.query_max(left, right-1) - st.query_min(left, right-1)
                heapq.heappush(pq, (-new_val, left, right-1))

        return ans